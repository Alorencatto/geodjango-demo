#

#


## Instalando o spatiallite
`apt install libsqlite3-mod-spatialite`

## Postgis
`
docker run --name=postgis -d -e POSTGRES_USER=user001 -e POSTGRES_PASS=123456789 -e POSTGRES_DBNAME=gis -p 5433:5432 kartoza/postgis
`

## Importando um shapefile
```
# Inspecionando o shapefile
ogrinfo geo_export_260ff6e1-c4bf-45d2-b17d-45d9e8fb6dc2.shp

# Informações sobre o atributo do shapefile
ogrinfo -so geo_export_260ff6e1-c4bf-45d2-b17d-45d9e8fb6dc2.shp geo_export_260ff6e1-c4bf-45d2-b17d-45d9e8fb6dc2

# Criando um modelo no geodjango / postgis 

  # Todos os arquivos auxiliares devem estar na mesma pasta
python manage.py ogrinspect geo_export_260ff6e1-c4bf-45d2-b17d-45d9e8fb6dc2.shp Neighborhood --srid=4326 --mapping --multi

```

## Referências

-- Tutorial de markers
https://realpython.com/location-based-app-with-geodjango-tutorial/

-- Tutorial de shp
https://lvngd.com/blog/point-in-polygon-search-with-geodjango/