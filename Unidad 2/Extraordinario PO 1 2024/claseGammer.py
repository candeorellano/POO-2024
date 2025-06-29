class Gammer:
    __id:int
    __dni:int
    __nombre:str
    __apellido:str
    __alias:str
    __plan:str
    __importeBase:int
    __tiempoLimite:int

    def __init__(self, id, dni, nom, apell, alias, plan, impB, tiempoLim):
        self.__id = id
        self.__dni = dni
        self.__nombre = nom
        self.__apellido = apell
        self.__alias = alias
        self.__plan = plan
        self.__importeBase = impB
        self.__tiempoLimite = tiempoLim

    def getId(self):
        return self.__id
    
    def getDni(self):
        return self.__dni
    
    def getNombre(self):
        return self.__nombre
    
    def getApellido(self):
        return self.__apellido
    
    def getAlias(self):
        return self.__alias
    
    def getPlan(self):
        return self.__plan  
    
    def getImporteBase(self):
        return self.__importeBase
    
    def getTiempoLimite(self):
        return self.__tiempoLimite
    
    def __str__(self):
        return f"ID: {self.__id}, DNI: {self.__dni}, Nombre: {self.__nombre}, Apellido: {self.__apellido}, Alias: {self.__alias}, Plan: {self.__plan}, Importe Base: {self.__importeBase}, Tiempo Limite: {self.__tiempoLimite}"