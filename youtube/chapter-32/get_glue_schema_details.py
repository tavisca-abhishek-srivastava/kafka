import boto3

session = boto3.Session( region_name='us-east-1')

glue_client = session.client('glue')
#glue = boto3.client('glue')
response = glue_client.list_registries(
    MaxResults=23
)


schema_message = glue_client.get_schema_version(
    SchemaId={
        'SchemaName': 'consumerlagdemo-value',
        'RegistryName': 'pgsql_nrt_registry'
    },
    SchemaVersionNumber={
        'LatestVersion': True
    }
)
print(schema_message['SchemaDefinition'])

schema_def = glue_client.get_schema_by_definition(

     SchemaId={
        'SchemaArn': 'arn:aws:glue:us-east-1:928814396842:schema/pgsql_nrt_registry/consumerlagdemo-value',
        'SchemaName': 'consumerlagdemo-value',
        'RegistryName': 'pgsql_nrt_registry'
    },
    SchemaDefinition=schema_message['SchemaDefinition']
)
print(schema_def)