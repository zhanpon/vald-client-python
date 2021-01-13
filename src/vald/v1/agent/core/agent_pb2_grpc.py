# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from vald.v1.payload import payload_pb2 as vald_dot_v1_dot_payload_dot_payload__pb2


class AgentStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateIndex = channel.unary_unary(
                '/core.v1.Agent/CreateIndex',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Control.CreateIndexRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Empty.FromString,
                )
        self.SaveIndex = channel.unary_unary(
                '/core.v1.Agent/SaveIndex',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Empty.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Empty.FromString,
                )
        self.CreateAndSaveIndex = channel.unary_unary(
                '/core.v1.Agent/CreateAndSaveIndex',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Control.CreateIndexRequest.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Empty.FromString,
                )
        self.IndexInfo = channel.unary_unary(
                '/core.v1.Agent/IndexInfo',
                request_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Empty.SerializeToString,
                response_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Info.Index.Count.FromString,
                )


class AgentServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateIndex(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SaveIndex(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateAndSaveIndex(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def IndexInfo(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateIndex': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateIndex,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Control.CreateIndexRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Empty.SerializeToString,
            ),
            'SaveIndex': grpc.unary_unary_rpc_method_handler(
                    servicer.SaveIndex,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Empty.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Empty.SerializeToString,
            ),
            'CreateAndSaveIndex': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateAndSaveIndex,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Control.CreateIndexRequest.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Empty.SerializeToString,
            ),
            'IndexInfo': grpc.unary_unary_rpc_method_handler(
                    servicer.IndexInfo,
                    request_deserializer=vald_dot_v1_dot_payload_dot_payload__pb2.Empty.FromString,
                    response_serializer=vald_dot_v1_dot_payload_dot_payload__pb2.Info.Index.Count.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'core.v1.Agent', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Agent(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateIndex(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/core.v1.Agent/CreateIndex',
            vald_dot_v1_dot_payload_dot_payload__pb2.Control.CreateIndexRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SaveIndex(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/core.v1.Agent/SaveIndex',
            vald_dot_v1_dot_payload_dot_payload__pb2.Empty.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateAndSaveIndex(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/core.v1.Agent/CreateAndSaveIndex',
            vald_dot_v1_dot_payload_dot_payload__pb2.Control.CreateIndexRequest.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def IndexInfo(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/core.v1.Agent/IndexInfo',
            vald_dot_v1_dot_payload_dot_payload__pb2.Empty.SerializeToString,
            vald_dot_v1_dot_payload_dot_payload__pb2.Info.Index.Count.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
