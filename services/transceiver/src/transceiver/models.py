'''Models (Shared across services)

This is a temporary implementation. A shim-layer to be replaced bt Pydantic
models pre version 1.
'''

from typing import Any

# TODO: Convert to pydantic models: https://docs.pydantic.dev/latest/

class Server():
    '''Stand-In for a future Server Model.'''
    id: str = ''
    name: str = ''
    parse: int = 1
    respond: int = 1

    def mapping(self) -> dict[str, Any]:
        '''Future proofing this class.

        Returns:
            dict[str, Any]: Dictionary respresentation
        '''
        return {
            'id': self.id,
            'name': self.name,
            'parse': self.parse,
            'respond': self.respond,
        }

class Channel():
    '''Stand-In for a future Channel Model.'''
    id: str = ''
    name: str = ''
    server_id: str = ''
    parse: int = 1
    respond: int = 1

    def mapping(self) -> dict[str, Any]:
        '''Future proofing this class.

        Returns:
            dict[str, Any]: Dictionary respresentation
        '''
        return {
            'id': self.id,
            'name': self.name,
            'server_id': self.server_id,
            'parse': self.parse,
            'respond': self.respond
        }

class User():
    '''Stand-In for a future User Model'''
    id = None
    name = None
    parse = 1
    respond = 1

    def mapping(self) -> dict[str, Any]:
        '''Future proofing this class.

        Returns:
            dict[str, Any]: Dictionary respresentation
        '''
        return {
            'id': self.id,
            'name': self.name,
            'parse': self.parse,
            'respond': self.respond
        }

class Message():
    '''Stand-In for a future Message Model.'''

    JSON_TEMPLATE: dict = {
        'id': None,
        'time': None,
        'content': None,
        'read': None,
        'response': None,
        'origin': {
            'server': {
                'id': None,
                'name': None,
                'channel': {
                    'id': None,
                    'name': None,
                }
            }
        },
        'user': {
            'id': None,
            'bot': 0,
            'name': None,
            'nick': None,
            'avatar': None,
        },
        'objects': {
            'links': [],
            'attachments': []
        }
    }

    def mapping(self) -> dict[str, Any]:
        '''Future proofing this class.

        Returns:
            dict[str, Any]: Dictionary respresentation
        '''
        return self.JSON_TEMPLATE

class Attachment():
    '''Stand-In for a future Attachment Model.'''
    id: str  = ''
    url: str  = ''
    filename: str = ''

    def mapping(self) -> dict[str, Any]:
        '''Future proofing this class.

        Returns:
            dict[str, Any]: Dictionary respresentation
        '''
        return {
            'id': self.id,
            'url': self.url,
            'filename': self.filename
        }
