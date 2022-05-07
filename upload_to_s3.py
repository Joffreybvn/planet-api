from os import environ
from pathlib import Path
import boto3

session = boto3.Session(
    aws_access_key_id=environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=environ.get('AWS_SECRET_ACCESS_KEY'),
)

s3 = session.resource('s3')

build_folder = './_site'
for path in Path(build_folder).rglob('*'):
    if path.is_file():

        s3.meta.client.upload_file(
            str(path),
            'planet.joffreybvn.be',
            str(path.relative_to(build_folder)),
            ExtraArgs={'ContentType': f'text/{path.suffix[1:]}'}
        )
