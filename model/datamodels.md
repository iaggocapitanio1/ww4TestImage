# Owner

Identifies a clinet (Owner of a project)
-  `id`: Client Identifier
   -  Attribute type: **Property**. 
   -  Required
-  `clientTypeInstitution`: Type of client -> True identifies an institutional client. False identifies a singular client
   -  Attribute type: **Property**. 
   -  Optional
-  `legalName`: Institution legal name
   -  Attribute type: **Property**. [Organization](https://schema.org/Organization)
   -  Optional
-  `givenName`: Client first name
   -  Attribute type: **Property**. [Person](https://schema.org/Person)
   -  Optional
-  `familyName`: Client last name
   -  Attribute type: **Property**. [Person](https://schema.org/Person)
   -  Optional
-  `taxId`: Client/Institution Tax ID
   -  Attribute type: **Property**. [Person](https://schema.org/Person)
   -  Required
-  `address`: The client's address
   -  Attribute type: **Property**. [address](https://schema.org/address)
   -  Required
-  `email`: Contact email address
   -  Attribute type: **Property**. [email](https://schema.org/email)
   -  Required
-  `telephone`: Mobile or telephone contact
   -  Attribute type: **Property**. [telephone](https://schema.org/telephone)
   -  Required
-  `buysTo`: Identification the addres that will recieve the oreder name
   -  Attribute type: **Relationship**. 
   -  Optional



# Project

Contains the information of a project
-  `id`: Projects id Identifier
   -  Attribute type: **Property**. 
   -  Required
-  `name`: Project name
   -  Attribute type: **Property**. [name](https://schema.org/name)
   -  Required
-  `category`: Movel type
   -  Attribute type: **Property**. 
   -  Optional
-  `status`: Indicates the actual workers station * `waiting` - Projects budget approved * `working` - Projects parts are already in the factorys floor * `finished` - Projects parts are all done * `assembly` - Projects parts are being assembled in the test zone * `expedition` - The request from a client is already out from the factory. One of : `Waiting`, `working`, `finished`, `assembly`, `expedition`.
   -  Attribute type: **Property**. 
   -  Optional
-  `nestingTag`: Identification of the final tag to past in wood part originated on nesting station
   -  Attribute type: **Relationship**. 
   -  Optional
-  `producedBy`: Identification of the operators giveName that are working in specific project Name
   -  Attribute type: **Relationship**. 
   -  Optional
-  `orderBy`: Identification of the owner name associated to the project with status in execution
   -  Attribute type: **Relationship**. 
   -  Optional
-  `acessories`: Identification of all nedded acessories for specific project
   -  Attribute type: **Relationship**. 
   -  Optional
-  `part`: Identification of the parts for a specific project comming from cut list
   -  Attribute type: **Relationship**. 
   -  Optional
-  `assemblyBy`: Identification assembled parts belong to some project made for some worker
   -  Attribute type: **Relationship**. 
   -  Optional
-  `expedition`: Identification the addres that will recieve the oreder name
   -  Attribute type: **Relationship**. 
   -  Optional



# Part

Identifies the part-name atributes that belongs to a specific project - Lista de Corte -
-  `id`: Unic Identifier of a Part of a Project
   -  Attribute type: **Property**. 
   -  Required
-  `partName`: REF PEÇA (A)
   -  Attribute type: **Property**. 
   -  Required
-  `sort`: TIPO (B)
   -  Attribute type: **Property**. 
   -  Required
-  `material`: MATERIAL (C)
   -  Attribute type: **Property**. 
   -  Required
-  `amount`: QUANTIDADE (D)
   -  Attribute type: **Property**. 
   -  Required
-  `length`: COMPRIMENTO (E)
   -  Attribute type: **Property**. 
   -  Optional
-  `width`: LARGURA (F)
   -  Attribute type: **Property**. 
   -  Required
-  `thickness`: ESPESSURA (G)
   -  Attribute type: **Property**. 
   -  Required
-  `tag`: ETIQUETA (H)
   -  Attribute type: **Property**. 
   -  Required
-  `nestingFlag`: NESTING (I)
   -  Attribute type: **Property**. 
   -  Optional
-  `cncFlag`: CNC (J)
   -  Attribute type: **Property**. 
   -  Optional
-  `f2`: FURO FACE 2 (K)
   -  Attribute type: **Property**. 
   -  Optional
-  `f3`: FURO FACE 3 (L)
   -  Attribute type: **Property**. 
   -  Optional
-  `f4`: FURO FACE 4 (M)
   -  Attribute type: **Property**. 
   -  Optional
-  `f5`: FURO FACE 5 (N)
   -  Attribute type: **Property**. 
   -  Optional
-  `veio`: VEIO (O)
   -  Attribute type: **Property**. 
   -  Optional
-  `orla2`: ORLA2 (P)
   -  Attribute type: **Property**. 
   -  Optional
-  `orla3`: ORLA3 (Q)
   -  Attribute type: **Property**. 
   -  Optional
-  `orla4`: ORLA4 (R)
   -  Attribute type: **Property**. 
   -  Optional
-  `orla5`: ORLA5 (S)
   -  Attribute type: **Property**. 
   -  Optional
-  `observation`: Observation (T)
   -  Attribute type: **Property**. 
   -  Optional
-  `weight`: PESO (U)
   -  Attribute type: **Property**. 
   -  Optional
-  `opcnc`: OPCNC (V)
   -  Attribute type: **Property**. 
   -  Optional
-  `belongsTo`: Identifies the project to wich the part belongs
   -  Attribute type: **Relationship**. 
   -  Optional
-  `image`: 
   -  Attribute type: **Property**. 
   -  Optional



## Examples

### OK


