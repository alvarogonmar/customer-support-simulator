class TicketHashMap:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.table = [[] for _ in range(capacity)]


    # Debe recibir un ID y devolver el índice correspondiente dentro del array.
    # Pista: ya conoces la fórmula ticket_id % capacity.
    def _hash(self, ticket_id):
        index = ticket_id % self.capacity
        return index 

    def insert(self, ticket):
        index = self._hash(ticket.id)
        bucket = self.table[index]

        for existing_ticket in bucket:
            if existing_ticket.id == ticket.id:
                return False

        bucket.append(ticket)
        self.size += 1

        if self.get_load_factor() > 0.75:
            self._resize()

        return True


    # Debe hacer lo siguiente:
    # 1. Calcular el índice usando _hash(ticket_id).
    # 2. Obtener el bucket correspondiente.
    # 3. Recorrer el bucket buscando un ticket cuyo id coincida.
    # 4. Devolver el objeto Ticket si lo encuentra.
    # 5. Devolver None si no existe.

    def get(self, ticket_id):
        index = self._hash(ticket_id)
        bucket = self.table[index]

        for existing_ticket in bucket:
            if existing_ticket.id == ticket_id:
                return existing_ticket

        return None

    def delete(self, ticket_id):
        # 1. Calcular el índice
        # 2. Obtener el bucket
        index = self._hash(ticket_id)
        bucket = self.table[index]

        # 3. Recorrer los tickets del bucket
        # 4. Encontrar el ticket con el ID solicitado
        for i, existing_ticket in enumerate(bucket):
            if existing_ticket.id == ticket_id:
                bucket.pop(i)
                self.size -= 1
                return True
        # 5. Eliminarlo y devolver True
        # 6. Si no existe, devolver False
        return False

    def get_load_factor(self):
    # Tu código aquí
        return self.size / self.capacity
    def _resize(self):
        # 1. Guardar la tabla anterior
        old_table = self.table

        # 2. Duplicar la capacidad
        self.capacity *= 2

        # 3. Crear una nueva tabla vacía
        self.table = [[] for _ in range(self.capacity)]

        # 4. Recorrer cada bucket de la tabla anterior
        for bucket in old_table:
            for ticket in bucket:
                index = self._hash(ticket.id)
                self.table[index].append(ticket)

        pass