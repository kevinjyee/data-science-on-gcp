from __future__ import absolute_import

import argparse
import logging

import apache_beam as beam


def run(argv=None):
    """Build and run the pipeline."""

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input_topic', dest='input_topic', required=True,
        help='Input PubSub topic of the form "projects/<project>/topics/<topic>".')

    parser.add_argument(
        '--output_topic', dest='output_topic', required=True,
        help='Output PubSub topic of the form "projects/<project>/topics/<topic>".')



    known_args, pipeline_args = parser.parse_known_args(argv)

    with beam.Pipeline(argv=pipeline_args) as p:

        # Read the text file[pattern] into a PCollection.
        lines = p | beam.io.ReadStringsFromPubSub(known_args.input_topic)

        print(lines)
        # Capitalize the characters in each line.
        transformed = (lines
                       | 'capitalize' >> (beam.Map(lambda x: x.upper())))



        transformed | beam.io.WriteStringsToPubSub(known_args.output_topic)
if __name__ == '__main__':
    logging.getLogger().setLevel(logging.INFO)
    run()
~                   
