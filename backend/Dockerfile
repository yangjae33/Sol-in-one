FROM adoptopenjdk/openjdk11
CMD ["./mvnw", "clean", "package"]
ARG JAR_FILE_PATH=target/*.jar
RUN ["pwd"]
COPY ${JAR_FILE_PATH} backend-0.0.1-SNAPSHOT.jar
ENTRYPOINT ["java", "-jar", "backend-0.0.1-SNAPSHOT.jar"]