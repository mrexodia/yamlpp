import ruamel.yaml
import sys


original_write_comment = None
already_written = set()


def hook_write_comment(emitter, comment, pre=False):
    global already_written, original_write_comment
    if comment.value.isspace():  # whitespace-only comments
        if comment not in already_written:
            already_written.add(comment)
            original_write_comment(emitter, comment, pre)
    else:
        original_write_comment(emitter, comment, pre)


def yamlpp(infile, outfile):
    global original_write_comment
    yaml = ruamel.yaml.YAML()
    yaml.Constructor.flatten_mapping = ruamel.yaml.SafeConstructor.flatten_mapping
    original_write_comment = yaml.Emitter.write_comment
    yaml.Emitter.write_comment = hook_write_comment
    yaml.default_flow_style = False
    yaml.allow_duplicate_keys = True
    yaml.width = 4096
    yaml.block_seq_indent = 2
    yaml.representer.ignore_aliases = lambda x: True
    yaml.dump(yaml.load(infile), outfile)


def main():
    if len(sys.argv) < 2:
        print("usage: yamlpp my.yml [pp.yml]")
        sys.exit(1)
    with open(sys.argv[1], "r") as infile:
        if len(sys.argv) > 2:
            with open(sys.argv[2], "w") as outfile:
                yamlpp(infile, outfile)
        else:
            yamlpp(infile, sys.stdout)


if __name__ == "__main__":
    main()
