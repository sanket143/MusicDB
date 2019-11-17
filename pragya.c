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
	printf("WHERE DO YOU WANT TO INSERT?\n1. seller\n2. buyer\n3. agent\n4. Other\n");
	printf("Choose the entity: ");
	scanf("%d",&choice);
	c=getchar();
	switch(choice){
		case 1:{
			
			char seller_id[20], seller_name[20], seller_contact_no[20], seller_emailid[100];
			printf("Seller_ID: ");
			scanf ("%[^\n]%*c", seller_id);
			printf("Seller_Name: ");
			scanf ("%[^\n]%*c", seller_name);
			printf("Seller_Contact_NO.: ");
			scanf ("%[^\n]%*c", seller_contact_no);
			printf("Seller_emailID: ");
			scanf ("%[^\n]%*c", seller_emailid);

			
			strcpy(query,"Insert into SellerDetails  (");			
			res = PQexec(conn, "select max(seller_id) from SellerDetails;");
			if (PQresultStatus(res) != PGRES_TUPLES_OK) {
       				printf("Failed to assign PrisonerDetails!\n");
        			PQclear(res);
    			}
			else{
				strcpy(seller_id,PQgetvalue(res, 0, 0));
				seller_id=seller_id+1;
			}
			fflush(stdout);
		
			/*CODE TO GENERATE INSERT QUERY IN BACK GROUND*/
			sprintf(buf,"%c",seller_id);
			strcat(query, buf);
			strcat(query,",'");
			strcat(query,seller_name);
			strcat(query,"','");
			strcat(query,seller_contact_no);
			strcat(query,"',");
			strcat(query,seller_emailid);			
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
			char buyer_id[20], buyer_name[20], buyer_contact_no[20], buyer_emailid[100], agent_id[20];
			printf("Buyer_ID: ");
			scanf ("%[^\n]%*c", buyer_id);
			printf("Buyer_Name: ");
			scanf ("%[^\n]%*c", buyer_name);
			printf("Buyer_Contact_NO.: ");
			scanf ("%[^\n]%*c", buyer_contact_no);
			printf("Buyer_emailID: ");
			scanf ("%[^\n]%*c", buyer_emailid);
			printf("Agent_ID: ");
			scanf ("%[^\n]%*c", agent_id);

			
			strcpy(query,"Insert into BuyerDetails  (");			
			res = PQexec(conn, "select max(buyer_id) from BuyerDetails;");
			if (PQresultStatus(res) != PGRES_TUPLES_OK) {
       				printf("Failed to assign PrisonerDetails!\n");
        			PQclear(res);
    			}
			else{
				strcpy(seller_id,PQgetvalue(res, 0, 0));
				buyer_id=buyer_id+1;
			}
			fflush(stdout);
		
			/*CODE TO GENERATE INSERT QUERY IN BACK GROUND*/
			sprintf(buf,"%c",buyer_id);
			strcat(query, buf);
			strcat(query,",'");
			strcat(query,buyer_name);
			strcat(query,"','");
			strcat(query,buyer_contact_no);
			strcat(query,"',");
			strcat(query,buyer_emailid);		
			strcat(query,"',");
			strcat(query,agent_id);	
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
		case 3:{
			char seller_id[20], seller_name[20], seller_contact_no[20], seller_emailid[100];
			printf("Seller_ID: ");
			scanf ("%[^\n]%*c", seller_id);
			printf("Seller_Name: ");
			scanf ("%[^\n]%*c", seller_name);
			printf("Seller_Contact_NO.: ");
			scanf ("%[^\n]%*c", seller_contact_no);
			printf("Seller_emailID: ");
			scanf ("%[^\n]%*c", seller_emailid);

			
			strcpy(query,"Insert into AgentDetails  (");			
			res = PQexec(conn, "select max(seller_id) from AgentDetails;");
			if (PQresultStatus(res) != PGRES_TUPLES_OK) {
       				printf("Failed to assign PrisonerDetails!\n");
        			PQclear(res);
    			}
			else{
				strcpy(agent_id,PQgetvalue(res, 0, 0));
				agent_id=agent_id+1;
			}
			fflush(stdout);
		
			/*CODE TO GENERATE INSERT QUERY IN BACK GROUND*/
			sprintf(buf,"%c",agent_id);
			strcat(query, buf);
			strcat(query,",'");
			strcat(query,agent_name);
			strcat(query,"','");
			strcat(query,agent_contact_no);
			strcat(query,"',");
			strcat(query,agent_emailid);			
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
void select_query() {
	printf("Enter Select Query: ");
	scanf("%c",&temp);
	scanf("%[^\n]s",q);
    	res = PQexec(conn, q);
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
    	conn = PQconnectdb("user=postgres password=super_spider dbname=postgres");
	if (PQstatus(conn) == CONNECTION_BAD) {
        	fprintf(stderr, "Connection to database failed: %s\n",
            	PQerrorMessage(conn));
		exit(1);
    	}
	printf("CONNECTED TO DATABASE!\n");
	PQexec(conn, "set search_path to ieee;");
	printf("SEARCH_PATH SET!\n");
	printf("\nChoose Option: \n");
	printf("1. Insert\n");
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
		printf("1. Insert\n");
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
