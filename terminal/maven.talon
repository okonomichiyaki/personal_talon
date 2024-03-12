tag: terminal
-
maven clean: "mvn clean \n"
maven clean test|maven test: "mvn clean test \n"
maven (install|package): "mvn clean package install -DskipTests=true \n"
maven dependency tree: "mvn compile dependency:tree \n"
maven dependency resolve: "mvn compile dependency:resolve \n"
maven compile: "mvn compile \n"
