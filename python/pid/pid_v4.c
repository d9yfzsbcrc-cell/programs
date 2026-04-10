/* Programa de control de un sistema con PID
	Compilar con:		gcc pid.c tiempo.c -o pid -lpthread 
		
	Ejecutar con: 		./pid
*/


// #include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>
#include "tiempo.h"
#include <sys/stat.h>
#include <fcntl.h>
#include <errno.h>


int main (void)
{
	
	int u = 1;
	int tiempoej, iteracion, i;
	float ts;
	int tsms;
	unsigned long tiempo;
	
	float *accontrol = NULL;
	float *referencia = NULL;
	float *error = NULL;
	float *salida = NULL;

	printf("\nEnter the simulation time: ");
  	scanf("%d",&tiempoej);

  	printf("\nEnter the sampling time in seconds: ");
  	scanf("%f",&ts);
	tsms = (int)(ts * 1000);
	int dimarray = (int)(tiempoej / ts);

	accontrol = calloc(dimarray, sizeof *accontrol);
	referencia = calloc(dimarray, sizeof *referencia);
	error = calloc(dimarray, sizeof *error);
	salida = calloc(dimarray, sizeof *salida);

	if (!accontrol || !referencia || !error || !salida)
	{
		perror("Error allocating arrays");
		free(accontrol);
		free(referencia);
		free(error);
		free(salida);
		return 1;
	}

	RESET_TMP();
	
	for (iteracion = 0; iteracion < dimarray; iteracion++)
	{
		if (iteracion==0)
		{
			error[iteracion] = 0.0;
			accontrol[iteracion] = 0;
			salida[iteracion] = 0; 
		}

		if (iteracion==1)
		{
			error[iteracion] = u - salida[iteracion-1];
			accontrol[iteracion] = accontrol[iteracion-1]+(18.86*error[iteracion])-(31.4396*error[iteracion-1]);
			salida[iteracion] = (1.81*salida[iteracion-1]) - (0.817*0.0f) + (0.007*accontrol[iteracion-1]);
		}
		if (iteracion>1)
		{
			error[iteracion] = u - salida[iteracion-1];
			accontrol[iteracion] = accontrol[iteracion-1]+(18.86*error[iteracion])-(31.4396*error[iteracion-1])+(12.7663*error[iteracion-2]);
			salida[iteracion] = (1.81*salida[iteracion-1]) - (0.817*salida[iteracion-2]) + (0.007*accontrol[iteracion-1]) + (0.0066*accontrol[iteracion-2]);
		}
		SLEEP_MSEC(tsms);
		
	}
	
	SET_TMP();
	tiempo = SEC_TRANS();
	printf("\n Simulation time: %lu seconds\n", tiempo);

	for (i=0; i<dimarray; i++)
	{
		referencia[i] = u;
	}

	// Save variables to file
	FILE *fp = fopen("/Users/rafa/Programas/python/pid/data_pid.txt", "w");
	if (fp == NULL)
	{
		perror("Error opening file");
		return 1;
	}


	fprintf(fp, "%.4f %d %d %d %d\n",ts, 0, 0, 0, 0);
	for (i = 0; i < dimarray; i++)
	{
		fprintf(fp, "%d %.6f %.6f %.6f %.6f\n", 
			i, referencia[i], error[i], accontrol[i], salida[i]);
	}
	
	fclose(fp);
	printf("\nData saved to data_pid.txt\n");

	char cmd[256];
	snprintf(cmd, sizeof cmd, "/Users/rafa/Programas/.venv/bin/python /Users/rafa/Programas/python/pid/graphpid.py");
	if (system(cmd) == -1)
	{
		perror("Error running Python script");
	}

	free(accontrol);
	free(referencia);
	free(error);
	free(salida);


	return 0;
}
	
	
	
