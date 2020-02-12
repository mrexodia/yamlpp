# yamlpp

Simple YAML preprocessor, resolves anchors. This is meant for preprocessing `.gitlab-ci.yml` files. The anchors will be preprocessed, so you can see what the file looks like if you wrote out everything by hand.

## Example

Here is `example.yml` (taken from https://docs.gitlab.com/ee/ci/yaml/#anchors):

```yml
.job_template: &job_definition
  script:
    - test project

.postgres_services:
  services: &postgres_definition
    - postgres # urmom
    - ruby

.mysql_services:
  services: &mysql_definition
    - mysql
    - ruby

test:postgres:
  <<: *job_definition
  services: *postgres_definition

test:mysql:
  <<: *job_definition
  services: *mysql_definition
```

If you run `yamlpp example.yml` the output will be:

```yml
.job_template:
  script:
    - test project

.postgres_services:
  services:
    - postgres
    - ruby

.mysql_services:
  services:
    - mysql
    - ruby

test:postgres:
  script:
    - test project
  services:
    - postgres
    - ruby

test:mysql:
  script:
    - test project
  services:
    - mysql
    - ruby
```