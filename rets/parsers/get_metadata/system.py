import xmltodict

from rets.models.metadata.system import System as SysModel
from rets.parsers.get_metadata.metadata_base import MetadataBase


class System(MetadataBase):

    def parse(self, response):

        xml = xmltodict.parse(response.text)
        base = xml.get('RETS', {}).get('METADATA', {}).get('METADATA-SYSTEM', {})

        system_obj = SysModel(session=self.session)

        configuration = self.session.configuration

        if configuration.rets_version == '1.5':
            if base.get('System', {}).get('SystemID'):
                system_obj.system_id = str(base['System']['SystemID'])
            if base.get('System', {}).get('SystemDescription'):
                system_obj.system_description = str(base['System']['SystemDescription'])

        else:
            if base.get('SYSTEM', {}).get('@SystemDescription'):
                system_obj.system_id = str(base['SYSTEM']['@SystemID'])

            if base.get('SYSTEM', {}).get('@SystemDescription'):
                system_obj.system_description = str(base['SYSTEM']['@SystemDescription'])

            if base.get('SYSTEM', {}).get('@TimeZoneOffset'):
                system_obj.timezone_offset = str(base['SYSTEM']['@TimeZoneOffset'])

        if base.get('SYSTEM', {}).get('Comments'):
            system_obj.comments = base['SYSTEM']['Comments']

        if base.get('@Version'):
            system_obj.version = base['@Version']

        return system_obj
