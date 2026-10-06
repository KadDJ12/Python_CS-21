from abc import abstractmethod , ABC

class Document(ABC):
    @abstractmethod
    def render(self) -> str:
        pass


class Report(Document):
    def render(self) -> str:
        return "Report - rendered" 


class Invoice(Document):
    def render(self) -> str:
        return "Invoice - rendered"


class Contract(Document):
    def render(self):
        return 'Contract - rendered'


class Document_not_Found(Document): 
    def render(self) -> str:
        return "Помилка: невідомий тип документа"


class DocumentFactory():
    dict = {
        'report': Report,
        'invoice': Invoice,
        'contract': Contract
    }
    def create(doc_type:str) -> Document:
        document_class = DocumentFactory.dict.get(doc_type, Document_not_Found)
        return document_class()



types_to_render = ['report', 'invoice', 'contract', 'some_unknown_format']

for doc_type in types_to_render:
    document = DocumentFactory.create(doc_type)
    print(f"Запит '{doc_type}': {document.render()}")



