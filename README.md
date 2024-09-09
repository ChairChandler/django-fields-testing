# Description

<style>
  red {
    color: red;
  }
</style>

## Overview

Package allows to test django model fields, meta model fields and normal class fields by subclasing dedicated special classes and django test class.
Every single class created using subclassing API is dedicated to specified model field. Apart from basic
field information like name and type for specified model, we can also test if it was created with specified attributes. Attributes are predefined.

Example:

```python
from django.test import SimpleTestCase

class NameFieldTest(ModelFieldTest, SimpleTestCase):
    model = User
    field_name = 'name'
    field_type = TextField
    default = ''
    primary_key = True

class UppercasedUsernameFieldTest(ClassFieldTest, SimpleTestCase):
    klass = User
    field_name = 'USERNAME_FIELD'
    value = 'email'

class ConstraintsFieldTest(MetaFieldTest, SimpleTestCase):
    klass = User
    field_name = 'constraints'
    value = [
        models.UniqueConstraint(
            fields=['telephone_prefix', 'telephone_number'],
            name='telephone_number_with_prefix_unique'
        )
    ]
```

Model field tests currently support the following attributes for fields:

- primary_key
- default
- verbose_name
- unique
- max_length
- validators
- help_text
- null
- blank

## Source code

**src** directory contains files dedicated to one of the special field testing class.

## Testing

**tests** directory contains files dedicated to testing one of the special field testing class.

To run tests, run script **run_tests.sh** inside **scripts** directory. It will generates unit tests report and coverage report inside **reports** directory.

## Building

To build a package run **run_build.sh** inside **scripts** directory. It will generate **whl** package file inside **dist** directory.

## Installation

Being inside package base directory run
> pip install dist/<red><package_name></red>.whl
