# swagger Examples - Adding generic router/switch
#
# This script uses an input ZIP file to add generic router/switch
# To add generic router/switch data source for currently unsupported switch/router.
# run this script with the param --zip_file_path (path for ZIP file created using network-insight-sdk-generic-datasources)
# proxy_ip and ip or fqdn of physical device..


import json
import logging

import swagger_client

from swagger_client.rest import ApiException
import swagger_client.models.data_source_type as data_source_type

import init_api_client
import utilities

logger = logging.getLogger("vrni_sdk")


def get_add_request_body(args, proxy_id):
    api_request_body = {"proxy_id": "{}".format(proxy_id),
                        "ip": "{}".format(args.device_ip_or_fqdn),
                        "entity_type": "UANIDataSource",
                        "nickname": "{}".format(args.device_ip_or_fqdn)}
    return api_request_body


def get_node_entity_id(api_client, proxy_ip=None):
    infrastructure_api = swagger_client.InfrastructureApi(api_client=api_client)
    node_list = infrastructure_api.list_nodes()
    for entity in node_list.results:
        node = infrastructure_api.get_node(id=entity.id)
        if proxy_ip == node.ip_address:
            return node.id
    return None


def get_uani_datasource(data_source_api, ip=None):
    if not ip: return None
    data_source_list = data_source_api.list_uani()
    for datasource in data_source_list.results:
        ds = data_source_api.get_uani(id=datasource.entity_id)
        if ds.ip == ip or ds.fqdn == ip:
            return datasource
    return None


def main(api_client, args):

    # Create data source API client object
    data_source_api = swagger_client.DataSourcesApi(api_client=api_client)
    proxy_id = get_node_entity_id(api_client, args.proxy_ip)
    try:
        response = get_uani_datasource(data_source_api, args.device_ip_or_fqdn)
        if not response:
            response = data_source_api.add_uani(body=get_add_request_body(args, proxy_id))
            logger.info(
                    "Successfully added: {} {} : Response : {}".format(data_source_type, args.device_ip_or_fqdn, response))
        data_source_api.file_upload(id=response.entity_id, file=args.zip_file_path)
        auth_api = swagger_client.AuthenticationApi(api_client=api_client)
        auth_token = auth_api.create(api_client.cookie)
        logger.info(
                "Successfully uploaded zip file: {}".format(args.zip_file_path))
    except ApiException as e:
        logger.exception(
                "Failed adding data source: {} : Error : {} ".format(args.device_ip_or_fqdn, json.loads(e.body)))

def parse_arguments():
    parser = init_api_client.parse_arguments()
    parser.add_argument('--device_ip_or_fqdn', action='store', help='switch or router IP or fqdn', required=True)
    parser.add_argument('--proxy_ip', action='store', help='IP address of vRNI proxy', required=True)
    parser.add_argument("--zip_file_path", action="store", help="zip file generated by uani")
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_arguments()
    utilities.configure_logging("/tmp")
    api_client = init_api_client.get_api_client(args)
    main(api_client, args)
