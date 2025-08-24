import boto3
import json
from io import StringIO
import pandas as pd


s3_client = boto3.client("s3")
BUCKET = "ismb-data-lake"

CORS_HEADERS = {
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type,Authorization",
    "Access-Control-Allow-Methods": "OPTIONS,GET"
}


def lambda_handler(event, context):
    # Tratar requisições OPTIONS (preflight)
    if event.get("httpMethod") == "OPTIONS":
        return {
            "statusCode": 200,
            "headers": CORS_HEADERS,
            "body": json.dumps({"msg": "CORS preflight OK"})
        }

    indice_key = event.get("queryStringParameters", {}).get("indice") if event.get("queryStringParameters") else None
    if not indice_key:
        indice_key = event.get("indice")  # Caso venha pelo evento direto

    if not indice_key:
        return {
            "statusCode": 400,
            "headers": CORS_HEADERS,
            "body": json.dumps({"error": "Parâmetro 'indice' obrigatório"})
        }

    return handle_get(indice_key)


def handle_get(indice_key):
    try:
        obj = s3_client.get_object(Bucket=BUCKET, Key="curated/indice_ismb.csv")
        csv_content = obj["Body"].read().decode("utf-8")
        df = pd.read_csv(StringIO(csv_content))

        if indice_key == 'ismb':
            df = df.rename(columns={'dat_ref': 'data', 'indice_isbm': 'valor'})
            df = df[['data', 'valor']]
        if indice_key == 'A':
            df = df.rename(columns={'dat_ref': 'data', 'score_risco_credito': 'valor'})
            df = df[['data', 'valor']]
        if indice_key == 'B':
            df = df.rename(columns={'dat_ref': 'data', 'score_retorno_mercado': 'valor'})
            df = df[['data', 'valor']]
        if indice_key == 'C':
            df = df.rename(columns={'dat_ref': 'data', 'score_volatilidade_mercado': 'valor'})
            df = df[['data', 'valor']]
        if indice_key == 'D':
            df = df.rename(columns={'dat_ref': 'data', 'score_atividade_mercado': 'valor'})
            df = df[['data', 'valor']]
        if indice_key == 'E':
            df = df.rename(columns={'dat_ref': 'data', 'score_confianca_mercado': 'valor'})
            df = df[['data', 'valor']]
        if indice_key == 'F':
            df = df.rename(columns={'dat_ref': 'data', 'score_noticias': 'valor'})
            df = df[['data', 'valor']]

        df['valor'] = pd.to_numeric(df['valor'], errors='coerce').round(2)
        df["valor"] = df["valor"].fillna(0)
        data = df.to_dict(orient="records")

        return {
            "statusCode": 200,
            "headers": {**CORS_HEADERS, "Content-Type": "application/json"},
            "body": json.dumps(data, ensure_ascii=False)
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "headers": CORS_HEADERS,
            "body": json.dumps({"error": str(e)})
        }
