# @generated

# This file was generated by running `python -m dagster.grpc.compile`
# Do not edit this file directly, and do not attempt to recompile it using
# grpc_tools.protoc directly, as several changes must be made to the raw output

# pylint: disable=no-member, unused-argument

# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from . import api_pb2 as api__pb2


class DagsterApiStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ping = channel.unary_unary(
            '/api.DagsterApi/Ping',
            request_serializer=api__pb2.PingRequest.SerializeToString,
            response_deserializer=api__pb2.PingReply.FromString,
        )


class DagsterApiServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Ping(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DagsterApiServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'Ping': grpc.unary_unary_rpc_method_handler(
            servicer.Ping,
            request_deserializer=api__pb2.PingRequest.FromString,
            response_serializer=api__pb2.PingReply.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler('api.DagsterApi', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class DagsterApi(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Ping(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/api.DagsterApi/Ping',
            api__pb2.PingRequest.SerializeToString,
            api__pb2.PingReply.FromString,
            options,
            channel_credentials,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
