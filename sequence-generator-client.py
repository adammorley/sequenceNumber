#!/usr/bin/python

from __future__ import print_function

import grpc

import sequence_generator_pb2

def run():
    channel = grpc.insecure_channel('localhost:50000')
    stub = sequence_generator_pb2.SequenceNumberGeneratorStub(channel)
    response = stub.GenerateSequenceNumber(sequence_generator_pb2.q_SequenceNumber())
    print("Got a sequence number: " + str(response.sequenceNumber))


if __name__ == '__main__':
    run()
