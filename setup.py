# -*- coding: utf-8 -*-
import sys

from setuptools import setup

# Require Python 2.7.9 or higher or Python 3.4 or higher
if (sys.version_info[:3] < (2, 7, 9)) or ((sys.version_info[0] == 3) and sys.version_info[:2] < (3, 4)):
    raise ValueError('''PyXB requires:
  Python2 version 2.7.9 or later; or
  Python3 version 3.4 or later
(You have %s.)''' % (sys.version,))

setup(
    name='VantiveCommerceSDKv2',
    version='9.12.0',
    description='Vantiv eCommerce Python SDKv2',
    author='Vantiv eCommerce',
    author_email='SDKSupport@vantiv.com',
    url='https://developer.vantiv.com/community/ecommerce',
    packages=['vantivsdk', 'scripts'],
    install_requires=[
        'PyXB==1.2.5',
        'paramiko>=1.14.0',
        'requests>=2.13.0',
        'six>=1.10.0',
        'xmltodict>=0.10.2'
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Environment :: Web Environment',
        'Environment :: MacOS X'
        'Environment :: Plugins'
        'Environment :: Win32 (MS Windows)'
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent'
        'Operating System :: MacOS',
        'Operating System :: Microsoft',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7.9',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Office/Business :: Financial',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    entry_points={
        'console_scripts': [
            'vantiv_python_sdk_setup = scripts.vantiv_python_sdk_setup:main',
        ],
    },
    long_description='''Vantiv eCommerce Python SDKv2
=============================

.. _`Vantiv eCommerce`: https://developer.vantiv.com/community/ecommerce

About Vantiv eCommerce
----------------------
`Vantiv eCommerce`_ powers the payment processing engines for leading companies that sell directly to consumers through  internet retail, direct response marketing (TV, radio and telephone), and online services. Vantiv eCommerce is the leading authority in card-not-present (CNP) commerce, transaction processing and merchant services.


About this SDK
--------------
The Vantiv eCommerce Python SDKv2 is a Python implementation of the `Vantiv eCommerce`_ XML API. This SDK was created to make it as easy as possible to connect to and process payments through Vantiv eCommerce. This SDK utilizes the HTTPS protocol to securely connect to Vantiv eCommerce.  Using the SDK requires coordination with the Vantiv eCommerce team to obtain credentials for accessing our systems.

Each Python SDK release supports all of the functionality present in the associated Vantiv eCommerce XML version (e.g., 11.0.x supports Vantiv eCommerce XML v11.0). Please see the online copy of our XSD for Vantiv eCommerce XML to get more details on what the Vantiv eCommerce payments engine supports .

This SDK was implemented to support the Python2 version 2.7.9 and later, Python3 version 3.4 and later, and was created by Vantiv eCommerce. Its intended use is for online transaction processing utilizing your account on the Vantiv eCommerce payments engine.

See LICENSE file for details on using this software.

Source Code available from : https://github.com/LitleCo/litle-sdk-for-python/tree/9.10v2

Please contact `Vantiv eCommerce`_  to receive valid merchant credentials and determine which version of the SDK is right for your business requirements or if you require assistance in any other way.  You can reach us at sdksupport@Vantiv.com

Dependencies
------------
* pyxb v1.2.5 : http://pyxb.sourceforge.net/
* paramiko v1.14.0: http://www.paramiko.org/
* requests v2.13.0: http://docs.python-requests.org/en/master/
* six v1.10.0: https://github.com/benjaminp/six
* xmltodict 0.10.2: https://github.com/martinblech/xmltodict

Setup
-----
* Run vantiv_python_sdk_setup and answer the questions.

.. code:: bash

   vantiv_python_sdk_setup

Example
-------
.. code-block:: python

    #Example for SDKv2
    from __future__ import (print_function, unicode_literals)

    from vantivsdk import *

    # Initial Configuration object. If you have saved configuration in '.vantiv_python_sdk.conf' at system environment
    # variable: VANTIV_SDK_CONFIG or user home directory, the saved configuration will be automatically load.
    conf = utils.Configuration()

    # Configuration need following attributes for online request:
    # attributes = default value
    # user = ''
    # password = ''
    # merchantId = ''
    # reportGroup = 'Default Report Group'
    # url = 'https://www.testlitle.com/sandbox/communicator/online'
    # proxy = ''
    # print_xml = False

    # Initial Transaction.
    transaction = fields.authorization()
    transaction.orderId = '1'
    transaction.amount = 10010
    transaction.orderSource = 'ecommerce'
    transaction.id = 'ThisIsRequiredby11'

    # Create contact object
    contact = fields.contact()
    contact.name = 'John & Mary Smith'
    contact.addressLine1 = '1 Main St.'
    contact.city = 'Burlington'
    contact.state = 'MA'
    contact.zip = '01803-3747'
    contact.country = 'USA'
    # The type of billToAddress is contact
    transaction.billToAddress = contact

    # Create cardType object
    card = fields.cardType()
    card.number = '4100000000000000'
    card.expDate = '1215'
    card.cardValidationNum = '349'
    card.type = 'VI'
    # The type of card is cardType
    transaction.card = card

    # detail tax
    enhancedData = fields.enhancedData()
    enhancedData.customerReference = 'Litle'
    enhancedData.deliveryType = 'TBD'
    detailTax = fields.detailTax()
    detailTax.taxAmount = 100
    detailTax2 = fields.detailTax()
    detailTax2.taxAmount = 200
    # pyxb cannot bind multi occurs item, have to use pyxb.BIND
    enhancedData = pyxb.BIND(enhancedData.customerReference, enhancedData.deliveryType, detailTax, detailTax2)
    transaction.enhancedData = enhancedData

    # Send request to server and get response as dict
    response = online.request(transaction, conf)

    print('Message: %s' % response['authorizationResponse']['message'])
    print('LitleTransaction ID: %s' % response['authorizationResponse']['litleTxnId'])

    # Configuration need following attributes for batch request:
    # attributes = default value
    # sftp_username = ''
    # sftp_password = ''
    # sftp_url = ''
    # batch_requests_path = '/tmp/vantiv_sdk_batch_request'
    # batch_response_path = '/tmp/vantiv_sdk_batch_response'
    # fast_url = ''
    # fast_ssl = True
    # fast_port = ''
    # id = ''

    # Initial batch transactions container class
    transactions = batch.Transactions()

    # Add transaction to batch transactions container
    transactions.add(transaction)

    # Sent batch to server via socket and get response as dict
    response = batch.stream(transactions, conf)

    print('Message: %s' % response['batchResponse']['authorizationResponse']['message'])
    print('LitleTransaction ID: %s' % response['batchResponse']['authorizationResponse']['litleTxnId'])

''',
)