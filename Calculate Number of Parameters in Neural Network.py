def calculate_parameters(layers: list[dict]) -> int:
	"""
	Calculate the total number of trainable parameters in a neural network.

	Args:
		layers: List of dictionaries, each describing a layer.

	Returns:
		Total number of trainable parameters (int).
	"""
	# Your code here
	parameters = 0
	for i in layers:
		if i.get('bias', True) == True:
			match i["type"]:
				case "dense":
					parameters = parameters + i["input_size"] * i["output_size"] + i["output_size"]
				case "conv2d":
					parameters = parameters + i["in_channels"] * i["out_channels"] * i["kernel_size"] * i["kernel_size"] + i["out_channels"]
		else:
			match i["type"]:
				case "dense":
					parameters = parameters + i["input_size"] * i["output_size"]
				case "conv2d":
					parameters = parameters + i["in_channels"] * i["out_channels"] * i["kernel_size"] * i["kernel_size"]
	return parameters