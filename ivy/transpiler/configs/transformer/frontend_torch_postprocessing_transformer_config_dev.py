AXIS_MAP = {
    "NCHW": {
        "1D": {0: 0, 1: -1, -1: -1, -2: 0},
        "2D": {0: 0, 1: -1, 2: -2, -1: -1, -2: -2, -3: 0},
        "3D": {0: 0, 1: -1, 2: -2, 3: -3, -1: -1, -2: -2, -3: -3, -4: 0},
    }
}

# TODO: Use of torch_frontend here is not ideal.
# Best to deal with this inside the postprocessing transformer.
DTYPE_MAPPING = {
    "torch.dtype": "ivy.NativeDtype",
    "torch.device": "ivy.NativeDevice",
    "torch.int8": "ivy.int8",
    "torch.int16": "ivy.int16",
    "torch.int32": "ivy.int32",
    "torch.int64": "ivy.int64",
    "torch.uint8": "ivy.uint8",
    "torch.uint16": "ivy.uint16",
    "torch.uint32": "ivy.uint32",
    "torch.uint64": "ivy.uint64",
    "torch.bfloat16": "ivy.bfloat16",
    "torch.float16": "ivy.float16",
    "torch.float32": "ivy.float32",
    "torch.float": "ivy.float32",
    "torch.float64": "ivy.float64",
    "torch.complex64": "ivy.complex64",
    "torch.complex128": "ivy.complex128",
    "torch.bool": "ivy.bool",
    "torch.char": "ivy.int8",
    "torch.short": "ivy.int16",
    "torch.int": "ivy.int32",
    "torch.long": "ivy.int64",
    "torch.half": "ivy.float16",
    "torch.float": "ivy.float32",
    "torch.double": "ivy.float64",
    "torch_frontend.int8": "ivy.int8",
    "torch_frontend.int16": "ivy.int16",
    "torch_frontend.int32": "ivy.int32",
    "torch_frontend.int64": "ivy.int64",
    "torch_frontend.uint8": "ivy.uint8",
    "torch_frontend.uint16": "ivy.uint16",
    "torch_frontend.uint32": "ivy.uint32",
    "torch_frontend.uint64": "ivy.uint64",
    "torch_frontend.bfloat16": "ivy.bfloat16",
    "torch_frontend.float16": "ivy.float16",
    "torch_frontend.float32": "ivy.float32",
    "torch_frontend.float64": "ivy.float64",
    "torch_frontend.complex64": "ivy.complex64",
    "torch_frontend.complex128": "ivy.complex128",
    "torch_frontend.bool": "ivy.bool",
    "torch_frontend.char": "ivy.int8",
    "torch_frontend.short": "ivy.int16",
    "torch_frontend.int": "ivy.int32",
    "torch_frontend.long": "ivy.int64",
    "torch_frontend.half": "ivy.float16",
    "torch_frontend.float": "ivy.float32",
    "torch_frontend.double": "ivy.float64",
    "torch_frontend.torch_promotion_table": "torch_promotion_table",
    "ivy.functional.frontends.torch.int8": "ivy.int8",
    "ivy.functional.frontends.torch.int16": "ivy.int16",
    "ivy.functional.frontends.torch.int32": "ivy.int32",
    "ivy.functional.frontends.torch.int64": "ivy.int64",
    "ivy.functional.frontends.torch.uint8": "ivy.uint8",
    "ivy.functional.frontends.torch.uint16": "ivy.uint16",
    "ivy.functional.frontends.torch.uint32": "ivy.uint32",
    "ivy.functional.frontends.torch.uint64": "ivy.uint64",
    "ivy.functional.frontends.torch.bfloat16": "ivy.bfloat16",
    "ivy.functional.frontends.torch.float16": "ivy.float16",
    "ivy.functional.frontends.torch.float32": "ivy.float32",
    "ivy.functional.frontends.torch.float": "ivy.float32",
    "ivy.functional.frontends.torch.float64": "ivy.float64",
    "ivy.functional.frontends.torch.complex64": "ivy.complex64",
    "ivy.functional.frontends.torch.complex128": "ivy.complex128",
    "ivy.functional.frontends.torch.bool": "ivy.bool",
    "ivy.functional.frontends.torch.char": "ivy.int8",
    "ivy.functional.frontends.torch.short": "ivy.int16",
    "ivy.functional.frontends.torch.int": "ivy.int32",
    "ivy.functional.frontends.torch.long": "ivy.int64",
    "ivy.functional.frontends.torch.half": "ivy.float16",
    "ivy.functional.frontends.torch.float": "ivy.float32",
    "ivy.functional.frontends.torch.double": "ivy.float64",
    "ivy.functional.frontends.torch.int8": "ivy.int8",
    "ivy.functional.frontends.torch.torch_promotion_table": "torch_promotion_table",
}

ARRAY_AND_MODULE_MAPPING = {
    "nn.Module": "ivy.Module",
    "torch.nn.Module": "ivy.Module",
    "torch.nn.modules.module.Module": "ivy.Module",
    "ivy.functional.frontends.torch.nn.modules.module.Module": "ivy.Module",
    "nn.Parameter": "ivy.Variable",
    "torch.nn.Parameter": "ivy.Variable",
    "torch.nn.parameter.Parameter": "ivy.Variable",
    "ivy.functional.frontends.torch.nn.parameter.Parameter": "ivy.Variable",
    "torch.Tensor": "ivy.Array",
    "ivy.functional.frontends.torch.Tensor": "ivy.Array",
    "torch_frontend.Tensor": "ivy.Array",
}
