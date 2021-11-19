tag: terminal
-
maven clean: "mvn clean \n"
maven test: "mvn clean test \n"
maven (install|package): "mvn clean package install -DskipTests=true \n"
maven tree: "mvn dependency:tree \n"
maven (dependency resolve|dependency|resolve): "mvn dependency:resolve \n"
