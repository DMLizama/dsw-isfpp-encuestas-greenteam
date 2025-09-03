from personas.constants import ErrorCode
from exceptions import NotFound, BadRequest

class PersonaNoEncontrada(NotFound):
    DETAIL = ErrorCode.PERSONA_NO_ENCONTRADA

class EmailDuplicado(BadRequest):
    DETAIL = ErrorCode.EMAIL_DUPLICADO