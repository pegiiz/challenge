# challenge
ec2server.py es el script del servidor hosteado en aws
funciona como un proxy hacia S3, acepta curls para subir archivos y descargar con presigned urls


http://servidorec2/upldec2/<TU_BUCKET> ----> para subir un archivo: 
curl -F 'file=@/RUTA/DEL/ARCHIVO' http://servidorec2/upldec2/<TU_BUCKET>


curl http://servidorec2/dwlec2/<TU_BUCKET>/<TU_KEY> ----> para descargar un archivo, el servidor devolvera una presigned url, para descargar dicho archivo usando curl de nuevo o desde el navegador
en los endpoints se deben especificar la funcion a llamar seguida del bucket, y para descargar, especificar la key 


curl http://servidorec2/listfiles/<TU_BUCKET> --->para listar las keys en el bucket especificado, esta funcion devolvera un json listando los archivos que haya en el bucket




