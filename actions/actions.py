from typing import Any, Text, Dict, List
 
from rasa_sdk import Tracker, FormValidationAction, Action
from rasa_sdk.events import EventType
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
 
TEMAS = ["ciudadanía", "recaudación"]
DEPARTAMENTOS = ["acción social","hacienda", "finanzas"]
DESTINATARIOS = ["empresas", "personas físicas", "personas jurídicas"]
TRAMITES = ["Trámite 1", "Trámite 2", "Trámite 3", "Trámite 4"]
 

class ValidateBuscarTramiteForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_buscar_tramite_form"

    def validate_palabras_clave(
        self,
        slot_value: Any,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: DomainDict,
    ) -> Dict[Text, Any]:
        """Validate `palabras_clave` value."""
 
        dispatcher.utter_message(text=f"{slot_value} ")
        return {"palabras_clave": slot_value}
 

