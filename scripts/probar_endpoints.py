"""Prueba de humo de los 40 endpoints contra una API en ejecución.

Uso (con la API levantada):
    python scripts/probar_endpoints.py [URL_BASE]

Crea sus propios registros, los modifica y al final los elimina, así que no
toca los datos que ya existen. Imprime una tabla Markdown con los resultados.
"""
import json
import sys
import urllib.error
import urllib.request

URL_BASE = sys.argv[1] if len(sys.argv) > 1 else "http://localhost:8000"
ORIGEN_FRONTEND = "http://localhost:4200"

resultados = []


def pedir(metodo, ruta, cuerpo=None, cabeceras=None):
    datos = json.dumps(cuerpo).encode() if cuerpo is not None else None
    peticion = urllib.request.Request(
        URL_BASE + ruta, data=datos, method=metodo,
        headers={"Content-Type": "application/json", **(cabeceras or {})},
    )
    try:
        respuesta = urllib.request.urlopen(peticion)
    except urllib.error.HTTPError as error:
        respuesta = error
    with respuesta:
        cabeceras = {k.lower(): v for k, v in respuesta.headers.items()}
        texto = respuesta.read().decode()
        es_json = "json" in cabeceras.get("content-type", "")
        datos = json.loads(texto) if texto and es_json else None
        return respuesta.status, datos, cabeceras


def probar(grupo, metodo, ruta, esperado, cuerpo=None, comprobar=None):
    codigo, datos, cabeceras = pedir(metodo, ruta, cuerpo)
    ok = codigo == esperado
    nota = ""
    if ok and comprobar is not None:
        ok, nota = comprobar(datos)
    if not ok and not nota:
        nota = json.dumps(datos, ensure_ascii=False)[:120]
    resultados.append((grupo, metodo, ruta, esperado, codigo, ok, nota))
    return datos


def igual(campos):
    def comprobar(datos):
        distintos = {k: datos.get(k) for k, v in campos.items()
                     if datos.get(k) != v}
        return (not distintos), (f"distinto: {distintos}" if distintos else "")
    return comprobar


def es_lista(datos):
    return isinstance(datos, list), ""


def main():
    crud = "CRUD"

    # --- Creación (POST) ---
    esp = probar(crud, "POST", "/especies/", 201,
                 {"nombre": "Prueba especie", "descripcion": "temporal"})
    due = probar(crud, "POST", "/duenos/", 201,
                 {"nombre": "Prueba dueño", "telefono": "3000000000"})
    mas = probar(crud, "POST", "/mascotas/", 201,
                 {"nombre": "Prueba", "edad": 2, "especie_id": esp["id"],
                  "dueno_id": due["id"]})
    vet = probar(crud, "POST", "/veterinarios/", 201,
                 {"nombre": "Prueba vet", "especialidad": "General",
                  "telefono": "3111111111"})
    cit = probar(crud, "POST", "/citas/", 201,
                 {"fecha": "2026-11-10", "mascota_id": mas["id"],
                  "veterinario_id": vet["id"]},
                 igual({"estado": "pendiente", "fecha": "2026-11-10"}))
    con = probar(crud, "POST", "/consultas/", 201,
                 {"diagnostico": "Sano", "cita_id": cit["id"]},
                 igual({"observaciones": ""}))
    vac = probar(crud, "POST", "/vacunas/", 201,
                 {"nombre": "Rabia", "fecha_aplicacion": "2026-11-01",
                  "mascota_id": mas["id"]})
    tra = probar(crud, "POST", "/tratamientos/", 201,
                 {"medicamento": "Vitaminas", "duracion_dias": 5,
                  "consulta_id": con["id"]})

    ids = {
        "especies": esp["id"], "duenos": due["id"], "mascotas": mas["id"],
        "veterinarios": vet["id"], "citas": cit["id"],
        "consultas": con["id"], "vacunas": vac["id"],
        "tratamientos": tra["id"],
    }

    # --- Listado y detalle (GET) ---
    for recurso, registro_id in ids.items():
        probar(crud, "GET", f"/{recurso}/", 200, comprobar=es_lista)
        probar(crud, "GET", f"/{recurso}/{registro_id}", 200,
               comprobar=igual({"id": registro_id}))

    # --- Actualización (PUT), incluye valores 0 y "" ---
    cambios = {
        "especies": {"descripcion": ""},
        "duenos": {"direccion": "Calle 1", "telefono": "3222222222"},
        "mascotas": {"edad": 0},
        "veterinarios": {"especialidad": "Cirugía"},
        "citas": {"fecha": "2026-11-12"},
        "consultas": {"observaciones": "Control en un mes"},
        "vacunas": {"nombre": "Parvovirus"},
        "tratamientos": {"duracion_dias": 10},
    }
    for recurso, cuerpo in cambios.items():
        probar(crud, "PUT", f"/{recurso}/{ids[recurso]}", 200, cuerpo,
               igual(cuerpo))

    # --- Reglas de negocio y errores ---
    reglas = "Reglas"
    probar(reglas, "GET", f"/citas/{ids['citas']}", 200,
           comprobar=igual({"estado": "atendida"}))
    probar(reglas, "GET", "/especies/999999", 404)
    probar(reglas, "PUT", "/duenos/999999", 404, {"nombre": "X"})
    probar(reglas, "DELETE", "/vacunas/999999", 404)
    probar(reglas, "POST", "/mascotas/", 400,
           {"nombre": "X", "edad": 1, "especie_id": 999999,
            "dueno_id": ids["duenos"]})
    probar(reglas, "PUT", f"/vacunas/{ids['vacunas']}", 400,
           {"mascota_id": 999999})
    probar(reglas, "POST", "/consultas/", 409,
           {"diagnostico": "Duplicada", "cita_id": ids["citas"]})
    probar(reglas, "DELETE", f"/duenos/{ids['duenos']}", 409)
    probar(reglas, "DELETE", f"/consultas/{ids['consultas']}", 409)
    probar(reglas, "PUT", f"/mascotas/{ids['mascotas']}", 422,
           {"nombre": None})
    probar(reglas, "POST", "/especies/", 422, {"nombre": "   "})
    probar(reglas, "POST", "/citas/", 422,
           {"fecha": "15/09/2026", "mascota_id": ids["mascotas"],
            "veterinario_id": ids["veterinarios"]})

    codigo, _, cabeceras = pedir(
        "OPTIONS", "/especies/", cabeceras={
            "Origin": ORIGEN_FRONTEND,
            "Access-Control-Request-Method": "PUT",
        })
    permitido = cabeceras.get("access-control-allow-origin")
    resultados.append((
        "CORS", "OPTIONS", "/especies/ (preflight)", 200, codigo,
        codigo == 200 and permitido == ORIGEN_FRONTEND,
        f"allow-origin={permitido}",
    ))

    # --- Eliminación (DELETE), de hijos a padres ---
    orden = ["tratamientos", "vacunas", "consultas", "citas", "mascotas",
             "veterinarios", "duenos", "especies"]
    for recurso in orden:
        probar(crud, "DELETE", f"/{recurso}/{ids[recurso]}", 204)
    probar(reglas, "GET", f"/especies/{ids['especies']}", 404)

    imprimir_tabla()


def imprimir_tabla():
    print("| Grupo | Método | Ruta | Esperado | Obtenido | OK | Nota |")
    print("|---|---|---|---|---|---|---|")
    for grupo, metodo, ruta, esperado, codigo, ok, nota in resultados:
        marca = "sí" if ok else "NO"
        print(f"| {grupo} | {metodo} | {ruta} | {esperado} | {codigo} "
              f"| {marca} | {nota} |")
    fallos = sum(1 for r in resultados if not r[5])
    total_crud = sum(1 for r in resultados if r[0] == "CRUD")
    print(f"\nEndpoints CRUD probados: {total_crud}. "
          f"Pruebas totales: {len(resultados)}. Fallos: {fallos}.")
    sys.exit(1 if fallos else 0)


if __name__ == "__main__":
    main()
