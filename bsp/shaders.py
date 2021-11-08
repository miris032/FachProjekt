vertex_shader_source_unlit = """
#version 330
uniform mat4 modelViewProj;
uniform vec3 color;
in vec3 position;
out vec4 vColor;

void main() {
	gl_Position = modelViewProj * vec4(position, 1.0);
	vColor = vec4(color, 1);
}"""


fragment_shader_source_unlit = """
#version 330
in vec4 vColor;
out vec4 fragColor;

void main(void) {
	fragColor = vColor;
}"""

print(__name__)
