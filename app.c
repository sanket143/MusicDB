
/*
./dbms 
<RUN THE CODE>

Connection to database failed: could not connect to server: No such file or directory
	Is the server running locally and accepting
	connections on Unix domain socket "/var/run/postgresql/.s.PGSQL.5432"?
<ERROR>

sudo ln -s /tmp/.s.PGSQL.5432 /var/run/postgresql/.s.PGSQL.5432
<HOW TO SOLVE THE ERROR>

*/

/*
REQUIRED COMMANDS IN SEQUENCE
DIVYA@dell /etc/postgresql/9.5/main$ sudo gedit pg_hba.conf
<change peer to md5 everywhere in this file>

sudo gcc -o dbms name.c -I/usr/include/postgresql -lpq
<To Run the file named name.c>

*/


/*
	GROUP - 2.2
	Nirbhay Ram		- 201501068
	Rutvik Shah		- 201501083
	Karanraj Singh Saini	- 201501105
	Divyakumar Solanki	- 201501108
*/
#include <stdio.h>
#include <stdlib.h>
#include <libpq-fe.h>
#include <string.h>
#include <unistd.h>
#include<stdbool.h>
#include<sqlda.h>
int x;
char q[128],temp;
PGresult *res;
PGconn *conn;

void insert_choice() {
	int choice;
	char query[250],buf[20],c;
	printf("WHERE DO YOU WANT TO INSERT?\n1. IEEE Member\n2. Region\n3. Country\n4. Other\n");
	printf("Choose the entity: ");
	scanf("%d",&choice);
	c=getchar();
	switch(choice){
		case 1:{
			char name[100],email[100],query1[250];
			long long int mobile;
			int IsStudent;
			long long int ieeeno=0;
			char ieeenum[5];
			bool student;
			char s[10];
			printf("Name: ");
			scanf ("%[^\n]%*c", name);
			printf("Email: ");
			scanf ("%[^\n]%*c", email);
			printf("Mobile Number: ");
			scanf("%lld",&mobile);
			printf("Student(1) OR Professional(0)? ");
			scanf("%d",&IsStudent);
			if(IsStudent==1){
				student=true;
				strcpy(s,"true");
			}	
			else{
				student=false;
				strcpy(s,"false");
			}
			strcpy(query,"insert into ieeemember  values  (");
			/*Code to assign unique IEEE NUMBER to new Member*/			
			res = PQexec(conn, "select max(ieeeno) from ieeemember;");
			if (PQresultStatus(res) != PGRES_TUPLES_OK) {
       				printf("Failed to assign IEEE Number!\n");
        			PQclear(res);
    			}
			else{
				strcpy(ieeenum,PQgetvalue(res, 0, 0));
				int len = strlen(ieeenum);
				for(int i=0; i<len; i++){
					ieeeno = ieeeno * 10 + ( ieeenum[i] - '0' );
				}
				ieeeno=ieeeno+1;
			}
			fflush(stdout);
		
			/*CODE TO GENERATE INSERT QUERY IN BACK GROUND*/
			sprintf(buf,"%lld",ieeeno);
			strcat(query, buf);
			strcat(query,",'");
			strcat(query,name);
			strcat(query,"','");
			strcat(query,email);
			strcat(query,"',");
			sprintf(buf,"%lld",mobile);
			strcat(query,buf);
			strcat(query,",");
			strcat(query,s);			
			strcat(query,");");
			/*CODE TO RUN QUERY*/
			res = PQexec(conn, query);
		    	if(PQresultStatus(res) != PGRES_COMMAND_OK) {
				printf("\nError: %s\n",PQerrorMessage(conn));
    			}
			else {
				printf("AUTO-GENERATED INSERT STATEMENT ran Successfully!\n");
			}
    			PQclear(res);
			break;
		}
		case 2:{
			char regionid[5],regionname[100];
			printf("RegionID<Format: R##>: ");
			scanf ("%[^\n]%*c", regionid);
			printf("Region Name<Format: region_***>: ");
			scanf ("%[^\n]%*c", regionname);
			strcpy(query,"insert into region  values  ('");
			strcat(query, regionid);
			strcat(query,"','");
			strcat(query,regionname);
			strcat(query,"');");
			printf("%s\n",query);
			res = PQexec(conn, query);
		    	if(PQresultStatus(res) != PGRES_COMMAND_OK) {
				printf("\nError: %s\n",PQerrorMessage(conn));
    			}
			else {
				printf("AUTO-GENERATED INSERT STATEMENT ran Successfully!\n");
			}
    			PQclear(res);
			break;	
		}
		case 3:{
			char regionid[5],countryname[100];
			printf("RegionID<Format: R##>: ");
			scanf ("%[^\n]%*c", regionid);
			printf("Country Name: ");
			scanf ("%[^\n]%*c", countryname);
			strcpy(query,"insert into country values  ('");
			strcat(query, countryname);
			strcat(query,"','");
			strcat(query,regionid);
			strcat(query,"');");
			printf("%s\n",query);
			res = PQexec(conn, query);
		    	if(PQresultStatus(res) != PGRES_COMMAND_OK) {
				printf("\nError: %s\n",PQerrorMessage(conn));
    			}
			else {
				printf("AUTO-GENERATED INSERT STATEMENT ran Successfully!\n");
			}
    			PQclear(res);
			break;	
		}
		case 4:{
			printf("Write Insert Statement: ");
        		scanf("%[^\n]s",q);
    			res = PQexec(conn, q);
    			if(PQresultStatus(res) != PGRES_COMMAND_OK) {
				printf("\nError: %s\n",PQerrorMessage(conn));
		    	}
			else {
				printf("Insert Statement ran Successfully!\n");
			}
		    	PQclear(res);
			break;
		}
		default:{
			printf("Please choose from choices given above.\n");
		}
	}	
}
void delete_choice(){
	printf("Write Delete Statement: ");
	scanf("%c",&temp);
        scanf("%[^\n]s",q);
    	res = PQexec(conn, q);
    	if(PQresultStatus(res) != PGRES_COMMAND_OK) {
		printf("\nError: %s\n",PQerrorMessage(conn));
    	}
	else {
		printf("Delete Statement ran Successfully!\n");
	}
    	PQclear(res);
}
void update_choice(){
	printf("Write Update Statement: ");
	scanf("%c",&temp);
        scanf("%[^\n]s",q);
    	res = PQexec(conn, q);
    	if(PQresultStatus(res) != PGRES_COMMAND_OK) {
		printf("\nError: %s\n",PQerrorMessage(conn));
    	}
	else {
		printf("Update Statement ran Successfully!\n");
	}
    	PQclear(res);
}
void first_query(){

}
void select_query() {
	res = PQexec(conn, "SELECT songname FROM artist NATURAL JOIN isinalbum NATURAL JOIN album NATURAL JOIN song WHERE (artistname = 'The Chainsmokers' AND albumname = 'World War Joy');");
	if (PQresultStatus(res) != PGRES_TUPLES_OK) {
		printf("No data retrieved\n");
		PQclear(res);
	}
	else {
		int rows = PQntuples(res);
		int cols = PQnfields(res);
		printf("\n");
		for(int i=0; i<rows; i++) {
			for (int j=0;j<cols;j++) {
				printf("%s\t",PQgetvalue(res, i, j));
			}
		printf("\n");
		}
	}
	PQclear(res);
}
int main() {
    	conn = PQconnectdb("hostaddr=10.100.71.21 user=201701247 password=onlysanket dbname=201701247");
	if (PQstatus(conn) == CONNECTION_BAD) {
        	fprintf(stderr, "Connection to database failed: %s\n",
            	PQerrorMessage(conn));
		exit(1);
    	}
	printf("CONNECTED TO DATABASE!\n");
	PQexec(conn, "set search_path to music;");
	printf("SEARCH_PATH SET!\n");
	printf("\nChoose Option: \n");
	printf("1. Retrieve all the songs by a given Artist and given album name.\n");
	printf("2. Update\n");
	printf("3. Delete\n");	
	printf("4. Query\n");
	printf("0. Exit\n\n");
	printf("Enter Option: ");
	fflush(stdin);
	
	scanf("%d",&x);
	while(x){
		if (x==1) insert_choice();
		else if (x==2) update_choice();
		else if (x==3) delete_choice();	
		else if(x==4)	select_query();

		printf("\n\nChoose Option: \n");
		printf("1. Retrieve all the songs by a given Artist and given album name.\n");
		printf("2. Update\n");
		printf("3. Delete\n");	
		printf("4. Query\n");
		printf("0. Exit\n\n");
		printf("Enter Option: ");
		fflush(stdin);

		scanf("%d",&x);
	}
    	PQfinish(conn);
	return 0;
}
