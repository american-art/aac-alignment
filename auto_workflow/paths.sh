echo "Setting paths..."
# Make sure that AAC_ROOT points to correct directory
export AAC_ROOT=/opt
export KARMA_USER_HOME=$AAC_ROOT/aac-dependencies/karma
export HADOOP_HOME=$AAC_ROOT/aac-softwares/hadoop-2.6.0-cdh5.5.0
export SPARK_HOME=$AAC_ROOT/aac-softwares/spark-1.5.0-cdh5.5.0
export HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
export PATH=$HADOOP_HOME/bin:$SPARK_HOME/bin:$PATH
export SPARK_DIST_CLASSPATH=$HADOOP_HOME/etc/hadoop:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/common/*:$HADOOP_HOME/share/hadoop/hdfs:$HADOOP_HOME/share/hadoop/hdfs/lib/*:$HADOOP_HOME/share/hadoop/hdfs/*:$HADOOP_HOME/share/hadoop/yarn/lib/*:$HADOOP_HOME/share/hadoop/yarn/*:$HADOOP_HOME/share/hadoop/mapreduce/lib/*:$HADOOP_HOME/share/hadoop/mapreduce/*:$HADOOP_HOME/contrib/capacity-scheduler/*.jar:$HADOOP_HOME/share/hadoop/tools/lib/*:$HADOOP_HOME/share/hadoop/common/lib/*:$HADOOP_HOME/share/hadoop/tools/lib/*:$SPARK_HOME/lib/*