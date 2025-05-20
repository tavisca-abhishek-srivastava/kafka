import boto3
import json

# Initialize the boto3 client
glue_client = boto3.client('glue')

# Define the schema (e.g., a JSON string)
schema_definition = {
  "type": "record",
  "name": "Customer",
  "namespace": "com.example",
  "fields": [
    {"name": "id", "type": "int"},
    {"name": "name", "type": "string"},
    {"name": "email", "type": "string"}
  ]
}

# Register the schema in Glue Schema Registry
try:
  response = glue_client.register_schema(
      RegistryName="my-kafka-registry",  # Replace with your registry name
      SchemaName="customer_schema",  # Replace with your schema name
      SchemaDefinition=json.dumps(schema_definition),  # Schema as JSON
      SchemaType="AVRO",  # or "JSON", etc.
      Compatibility="BACKWARD" # or "FORWARD", "FULL"
  )
  print(f"Schema registered with ID: {response['SchemaId']}")
except Exception as e:
  print(f"Error registering schema: {e}")