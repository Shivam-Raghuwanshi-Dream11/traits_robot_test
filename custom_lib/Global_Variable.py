import logging

db_urls = {
    "db_url_load" : "jdbc:mysql://datahighway-aurora-master-load-181.dream11-load.local:3306",
    "db_url_stag" : "jdbc:mysql://datahighway-aurora-master-load-181.dream11-load.local:3306",
    "db_url_prod" : "jdbc:mysql://datahighway-aurora-master-load-181.dream11-load.local:3306",
    "db_url_local" : "jdbc:mysql://datahighway-aurora-master-load-181.dream11-load.local:3306",
}

source_dbs = {
    "source_dbs_load":"traits_db",
    "source_dbs_stag":"traits_db",
    "source_dbs_prod":"traits_db",
    "source_dbs_local":"traits_db",
}

db_user_names = {
    "db_user_name_load":"d11stag",
    "db_user_name_stag":"d11stag",
    "db_user_name_prod":"d11stag",
    "db_user_name_local":"d11stag"
}

db_passowrds ={
    "db_passowrds_load":"ENQmzHfQX4XR",
    "db_passowrds_stag":"ENQmzHfQX4XR",
    "db_passowrds_prod":"ENQmzHfQX4XR",
    "db_passowrds_local":"ENQmzHfQX4XR"
}

def set_db_url(envrionment):

    if (str(envrionment).lower()=="load"):
        return db_urls["db_url_load"]
    elif(str(envrionment).lower()=="stag"):
        return db_urls["db_url_stag"]
    elif(str(envrionment).lower()=="prod"):
        return db_urls["db_url_prod"]
    elif(str(envrionment).lower()=="local"):
        return db_urls["db_url_local"]

def set_db_user_name(envrionment):
    if (str(envrionment).lower() == "load"):
        return db_user_names["db_user_names_load"]
    elif (str(envrionment).lower() == "stag"):
        return db_user_names["db_user_names_stag"]
    elif (str(envrionment).lower() == "prod"):
        return db_user_names["db_user_names_prod"]
    elif (str(envrionment).lower() == "local"):
        return db_user_names["db_user_names_local"]

def set_source_db(envrionment):
    if (str(envrionment).lower() == "load"):
        return source_dbs["source_dbs_load"]
    elif (str(envrionment).lower() == "stag"):
        return source_dbs["source_dbs_stag"]
    elif (str(envrionment).lower() == "prod"):
        return source_dbs["source_dbs_prod"]
    elif (str(envrionment).lower() == "local"):
        return source_dbs["source_dbs_local"]

def set_db_passowrds(envrionment):
    if (str(envrionment).lower() == "load"):
        return source_dbs["source_dbs_load"]
    elif (str(envrionment).lower() == "stag"):
        return source_dbs["source_dbs_stag"]
    elif (str(envrionment).lower() == "prod"):
        return source_dbs["source_dbs_prod"]
    elif (str(envrionment).lower() == "local"):
        return source_dbs["source_dbs_local"]