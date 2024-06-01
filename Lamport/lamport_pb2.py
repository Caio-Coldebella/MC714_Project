# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: lamport.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='lamport.proto',
  package='lamport',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n\rlamport.proto\x12\x07lamport\"6\n\x0c\x45ventRequest\x12\x15\n\rlogical_clock\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\"&\n\rEventResponse\x12\x15\n\rlogical_clock\x18\x01 \x01(\x05\x32O\n\x0eLamportService\x12=\n\x0cResolveEvent\x12\x15.lamport.EventRequest\x1a\x16.lamport.EventResponseb\x06proto3'
)




_EVENTREQUEST = _descriptor.Descriptor(
  name='EventRequest',
  full_name='lamport.EventRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='logical_clock', full_name='lamport.EventRequest.logical_clock', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
    _descriptor.FieldDescriptor(
      name='message', full_name='lamport.EventRequest.message', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=b"".decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=26,
  serialized_end=80,
)


_EVENTRESPONSE = _descriptor.Descriptor(
  name='EventResponse',
  full_name='lamport.EventResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='logical_clock', full_name='lamport.EventResponse.logical_clock', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=82,
  serialized_end=120,
)

DESCRIPTOR.message_types_by_name['EventRequest'] = _EVENTREQUEST
DESCRIPTOR.message_types_by_name['EventResponse'] = _EVENTRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

EventRequest = _reflection.GeneratedProtocolMessageType('EventRequest', (_message.Message,), {
  'DESCRIPTOR' : _EVENTREQUEST,
  '__module__' : 'lamport_pb2'
  # @@protoc_insertion_point(class_scope:lamport.EventRequest)
  })
_sym_db.RegisterMessage(EventRequest)

EventResponse = _reflection.GeneratedProtocolMessageType('EventResponse', (_message.Message,), {
  'DESCRIPTOR' : _EVENTRESPONSE,
  '__module__' : 'lamport_pb2'
  # @@protoc_insertion_point(class_scope:lamport.EventResponse)
  })
_sym_db.RegisterMessage(EventResponse)



_LAMPORTSERVICE = _descriptor.ServiceDescriptor(
  name='LamportService',
  full_name='lamport.LamportService',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_start=122,
  serialized_end=201,
  methods=[
  _descriptor.MethodDescriptor(
    name='ResolveEvent',
    full_name='lamport.LamportService.ResolveEvent',
    index=0,
    containing_service=None,
    input_type=_EVENTREQUEST,
    output_type=_EVENTRESPONSE,
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
  ),
])
_sym_db.RegisterServiceDescriptor(_LAMPORTSERVICE)

DESCRIPTOR.services_by_name['LamportService'] = _LAMPORTSERVICE

# @@protoc_insertion_point(module_scope)
