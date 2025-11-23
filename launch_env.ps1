docker run --rm -it `
	   -p 8888:8888 `
	   --name fraud_detection_practice `
	   -v .\serverfiles:/home/jovyan/work `
	   quay.io/jupyter/pyspark-notebook
