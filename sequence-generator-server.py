#!/usr/bin/python
from concurrent import futures
import time

import grpc

import sequence_generator_pb2

import SequenceNumber

numberGenerator = SequenceNumber.NumberGenerator('sequenceNumber')

class SequenceNumberGenerator(sequence_generator_pb2.SequenceNumberGeneratorServicer):

    def GenerateSequenceNumber(self, request, context):
        number = numberGenerator.get()
        return sequence_generator_pb2.p_SequenceNumber(sequenceNumber=str(number))


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    sequence_generator_pb2.add_SequenceNumberGeneratorServicer_to_server(SequenceNumberGenerator(), server)
    server.add_insecure_port('[::]:50000')
    server.start()
    try:
        while True:
            time.sleep(60*60*24)
    except KeyboardInterupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
