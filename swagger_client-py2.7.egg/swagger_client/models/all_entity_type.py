# coding: utf-8

"""
    vRealize Network Insight API Reference

    vRealize Network Insight API Reference

    OpenAPI spec version: 1.1.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class AllEntityType(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    GROUP = "Group"
    BASESECURITYGROUP = "BaseSecurityGroup"
    BASEEVENT = "BaseEvent"
    BASEVIRTUALMACHINE = "BaseVirtualMachine"
    BASEFIREWALLRULE = "BaseFirewallRule"
    BASEIPSET = "BaseIPSet"
    BASEL2NETWORK = "BaseL2Network"
    BASEFIREWALL = "BaseFirewall"
    BASESERVICE = "BaseService"
    BASESERVICEGROUP = "BaseServiceGroup"
    BASEVNIC = "BaseVnic"
    VIRTUALMACHINE = "VirtualMachine"
    EC2INSTANCE = "EC2Instance"
    HOST = "Host"
    VNIC = "Vnic"
    VMKNIC = "Vmknic"
    VXLANLAYER2NETWORK = "VxlanLayer2Network"
    VLANL2NETWORK = "VlanL2Network"
    CLUSTER = "Cluster"
    SECURITYTAG = "SecurityTag"
    RESOURCEPOOL = "ResourcePool"
    NSXIPSET = "NSXIPSet"
    NSXTIPSET = "NSXTIPSet"
    EC2IPSET = "EC2IPSet"
    NSXSECURITYGROUP = "NSXSecurityGroup"
    NSGROUP = "NSGroup"
    EC2SECURITYGROUP = "EC2SecurityGroup"
    FLOW = "Flow"
    PROBLEMEVENT = "ProblemEvent"
    APPLICATION = "Application"
    TIER = "Tier"
    NSXFIREWALLRULE = "NSXFirewallRule"
    EC2SGFIREWALLRULE = "EC2SGFirewallRule"
    NSXREDIRECTRULE = "NSXRedirectRule"
    VCENTERMANAGER = "VCenterManager"
    NSXVMANAGER = "NSXVManager"
    NSXTMANAGER = "NSXTManager"
    CHECKPOINTMANAGER = "CheckpointManager"
    CHECKPOINTMDSMANAGER = "CheckpointMDSManager"
    BASEMANAGER = "BaseManager"
    BASEFIREWALLMANAGER = "BaseFirewallManager"
    BASENSXMANAGER = "BaseNSXManager"
    NSXSERVICE = "NSXService"
    EC2SERVICE = "EC2Service"
    NSSERVICE = "NSService"
    VPC = "VPC"
    CLOUDNETWORK = "CloudNetwork"
    AZUREVM = "AzureVM"
    AZURENSG = "AzureNSG"
    AZUREASG = "AzureASG"
    AZURENSGRULE = "AzureNSGRule"
    NSXDISTRIBUTEDFIREWALL = "NSXDistributedFirewall"
    EC2FIREWALL = "EC2Firewall"
    NSXSERVICEGROUP = "NSXServiceGroup"
    NSSERVICEGROUP = "NSServiceGroup"
    DISTRIBUTEDVIRTUALSWITCH = "DistributedVirtualSwitch"
    DISTRIBUTEDVIRTUALPORTGROUP = "DistributedVirtualPortgroup"
    VCDATACENTER = "VCDatacenter"
    DATASTORE = "Datastore"
    FOLDER = "Folder"
    NSXTFIREWALLRULE = "NSXTFirewallRule"
    NSXTFIREWALL = "NSXTFirewall"
    BASEGENERICFIREWALL = "BaseGenericFirewall"
    BASEGENERICFIREWALLRULE = "BaseGenericFirewallRule"
    CHECKPOINTFIREWALL = "CheckpointFirewall"
    CHECKPOINTFIREWALLRULE = "CheckpointFirewallRule"
    USERDEFINEDSUBNET = "UserDefinedSubnet"
    KUBERNETESSERVICE = "KubernetesService"

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        
    }

    attribute_map = {
        
    }

    def __init__(self):
        """
        AllEntityType - a model defined in Swagger
        """



    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, AllEntityType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
