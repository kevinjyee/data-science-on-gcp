#!/usr/bin/env bash
DIR=gs://pubsubtest1
PROJECT=sales-tools-200218
TOPIC=test1pubsub

python -m pubsub_test \
  --project $PROJECT \
  --runner DataflowRunner \
  --staging_location $DIR/staging \
  --temp_location $DIR/temp \
  --input_topic projects/$PROJECT/topics/$TOPIC
