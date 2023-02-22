# Generated by Django 4.1.7 on 2023-02-21 19:27

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Accounts",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("user_uuid", models.UUIDField(default=uuid.uuid4)),
                ("account_number", models.CharField(max_length=20, unique=True)),
                (
                    "currency",
                    models.CharField(
                        choices=[
                            ("AFN", "AFN"),
                            ("EUR", "EUR"),
                            ("ALL", "ALL"),
                            ("DZD", "DZD"),
                            ("USD", "USD"),
                            ("AOA", "AOA"),
                            ("XCD", "XCD"),
                            ("ARS", "ARS"),
                            ("AMD", "AMD"),
                            ("AWG", "AWG"),
                            ("AUD", "AUD"),
                            ("AZN", "AZN"),
                            ("BSD", "BSD"),
                            ("BHD", "BHD"),
                            ("BDT", "BDT"),
                            ("BBD", "BBD"),
                            ("BYN", "BYN"),
                            ("BZD", "BZD"),
                            ("XOF", "XOF"),
                            ("BMD", "BMD"),
                            ("INR", "INR"),
                            ("BTN", "BTN"),
                            ("BOB", "BOB"),
                            ("BOV", "BOV"),
                            ("BAM", "BAM"),
                            ("BWP", "BWP"),
                            ("NOK", "NOK"),
                            ("BRL", "BRL"),
                            ("BND", "BND"),
                            ("BGN", "BGN"),
                            ("BIF", "BIF"),
                            ("CVE", "CVE"),
                            ("KHR", "KHR"),
                            ("XAF", "XAF"),
                            ("CAD", "CAD"),
                            ("KYD", "KYD"),
                            ("CLP", "CLP"),
                            ("CLF", "CLF"),
                            ("CNY", "CNY"),
                            ("COP", "COP"),
                            ("COU", "COU"),
                            ("KMF", "KMF"),
                            ("CDF", "CDF"),
                            ("NZD", "NZD"),
                            ("CRC", "CRC"),
                            ("HRK", "HRK"),
                            ("CUP", "CUP"),
                            ("CUC", "CUC"),
                            ("ANG", "ANG"),
                            ("CZK", "CZK"),
                            ("DKK", "DKK"),
                            ("DJF", "DJF"),
                            ("DOP", "DOP"),
                            ("EGP", "EGP"),
                            ("SVC", "SVC"),
                            ("ERN", "ERN"),
                            ("SZL", "SZL"),
                            ("ETB", "ETB"),
                            ("FKP", "FKP"),
                            ("FJD", "FJD"),
                            ("XPF", "XPF"),
                            ("GMD", "GMD"),
                            ("GEL", "GEL"),
                            ("GHS", "GHS"),
                            ("GIP", "GIP"),
                            ("GTQ", "GTQ"),
                            ("GBP", "GBP"),
                            ("GNF", "GNF"),
                            ("GYD", "GYD"),
                            ("HTG", "HTG"),
                            ("HNL", "HNL"),
                            ("HKD", "HKD"),
                            ("HUF", "HUF"),
                            ("ISK", "ISK"),
                            ("IDR", "IDR"),
                            ("XDR", "XDR"),
                            ("IRR", "IRR"),
                            ("IQD", "IQD"),
                            ("ILS", "ILS"),
                            ("JMD", "JMD"),
                            ("JPY", "JPY"),
                            ("JOD", "JOD"),
                            ("KZT", "KZT"),
                            ("KES", "KES"),
                            ("KPW", "KPW"),
                            ("KRW", "KRW"),
                            ("KWD", "KWD"),
                            ("KGS", "KGS"),
                            ("LAK", "LAK"),
                            ("LBP", "LBP"),
                            ("LSL", "LSL"),
                            ("ZAR", "ZAR"),
                            ("LRD", "LRD"),
                            ("LYD", "LYD"),
                            ("CHF", "CHF"),
                            ("MOP", "MOP"),
                            ("MKD", "MKD"),
                            ("MGA", "MGA"),
                            ("MWK", "MWK"),
                            ("MYR", "MYR"),
                            ("MVR", "MVR"),
                            ("MRU", "MRU"),
                            ("MUR", "MUR"),
                            ("XUA", "XUA"),
                            ("MXN", "MXN"),
                            ("MXV", "MXV"),
                            ("MDL", "MDL"),
                            ("MNT", "MNT"),
                            ("MAD", "MAD"),
                            ("MZN", "MZN"),
                            ("MMK", "MMK"),
                            ("NAD", "NAD"),
                            ("NPR", "NPR"),
                            ("NIO", "NIO"),
                            ("NGN", "NGN"),
                            ("OMR", "OMR"),
                            ("PKR", "PKR"),
                            ("PAB", "PAB"),
                            ("PGK", "PGK"),
                            ("PYG", "PYG"),
                            ("PEN", "PEN"),
                            ("PHP", "PHP"),
                            ("PLN", "PLN"),
                            ("QAR", "QAR"),
                            ("RON", "RON"),
                            ("RUB", "RUB"),
                            ("RWF", "RWF"),
                            ("SHP", "SHP"),
                            ("WST", "WST"),
                            ("STN", "STN"),
                            ("SAR", "SAR"),
                            ("RSD", "RSD"),
                            ("SCR", "SCR"),
                            ("SLL", "SLL"),
                            ("SLE", "SLE"),
                            ("SGD", "SGD"),
                            ("XSU", "XSU"),
                            ("SBD", "SBD"),
                            ("SOS", "SOS"),
                            ("SSP", "SSP"),
                            ("LKR", "LKR"),
                            ("SDG", "SDG"),
                            ("SRD", "SRD"),
                            ("SEK", "SEK"),
                            ("CHE", "CHE"),
                            ("CHW", "CHW"),
                            ("SYP", "SYP"),
                            ("TWD", "TWD"),
                            ("TJS", "TJS"),
                            ("TZS", "TZS"),
                            ("THB", "THB"),
                            ("TOP", "TOP"),
                            ("TTD", "TTD"),
                            ("TND", "TND"),
                            ("TRY", "TRY"),
                            ("TMT", "TMT"),
                            ("UGX", "UGX"),
                            ("UAH", "UAH"),
                            ("AED", "AED"),
                            ("USN", "USN"),
                            ("UYU", "UYU"),
                            ("UYI", "UYI"),
                            ("UYW", "UYW"),
                            ("UZS", "UZS"),
                            ("VUV", "VUV"),
                            ("VES", "VES"),
                            ("VED", "VED"),
                            ("VND", "VND"),
                            ("YER", "YER"),
                            ("ZMW", "ZMW"),
                            ("ZWL", "ZWL"),
                            ("XBA", "XBA"),
                            ("XBB", "XBB"),
                            ("XBC", "XBC"),
                            ("XBD", "XBD"),
                            ("XTS", "XTS"),
                            ("XXX", "XXX"),
                            ("XAU", "XAU"),
                            ("XPD", "XPD"),
                            ("XPT", "XPT"),
                            ("XAG", "XAG"),
                        ],
                        max_length=5,
                    ),
                ),
                ("amount", models.DecimalField(decimal_places=2, max_digits=12)),
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "account_type",
                    models.CharField(
                        choices=[
                            ("CREDIT", "Credit"),
                            ("CURRENT", "Current"),
                            ("DEPOSIT", "Deposit"),
                            ("INTEREST", "Interest"),
                        ],
                        default="CURRENT",
                        max_length=8,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Transaction",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("amount", models.DecimalField(decimal_places=2, max_digits=12)),
                (
                    "currency",
                    models.CharField(
                        choices=[
                            ("AFN", "AFN"),
                            ("EUR", "EUR"),
                            ("ALL", "ALL"),
                            ("DZD", "DZD"),
                            ("USD", "USD"),
                            ("AOA", "AOA"),
                            ("XCD", "XCD"),
                            ("ARS", "ARS"),
                            ("AMD", "AMD"),
                            ("AWG", "AWG"),
                            ("AUD", "AUD"),
                            ("AZN", "AZN"),
                            ("BSD", "BSD"),
                            ("BHD", "BHD"),
                            ("BDT", "BDT"),
                            ("BBD", "BBD"),
                            ("BYN", "BYN"),
                            ("BZD", "BZD"),
                            ("XOF", "XOF"),
                            ("BMD", "BMD"),
                            ("INR", "INR"),
                            ("BTN", "BTN"),
                            ("BOB", "BOB"),
                            ("BOV", "BOV"),
                            ("BAM", "BAM"),
                            ("BWP", "BWP"),
                            ("NOK", "NOK"),
                            ("BRL", "BRL"),
                            ("BND", "BND"),
                            ("BGN", "BGN"),
                            ("BIF", "BIF"),
                            ("CVE", "CVE"),
                            ("KHR", "KHR"),
                            ("XAF", "XAF"),
                            ("CAD", "CAD"),
                            ("KYD", "KYD"),
                            ("CLP", "CLP"),
                            ("CLF", "CLF"),
                            ("CNY", "CNY"),
                            ("COP", "COP"),
                            ("COU", "COU"),
                            ("KMF", "KMF"),
                            ("CDF", "CDF"),
                            ("NZD", "NZD"),
                            ("CRC", "CRC"),
                            ("HRK", "HRK"),
                            ("CUP", "CUP"),
                            ("CUC", "CUC"),
                            ("ANG", "ANG"),
                            ("CZK", "CZK"),
                            ("DKK", "DKK"),
                            ("DJF", "DJF"),
                            ("DOP", "DOP"),
                            ("EGP", "EGP"),
                            ("SVC", "SVC"),
                            ("ERN", "ERN"),
                            ("SZL", "SZL"),
                            ("ETB", "ETB"),
                            ("FKP", "FKP"),
                            ("FJD", "FJD"),
                            ("XPF", "XPF"),
                            ("GMD", "GMD"),
                            ("GEL", "GEL"),
                            ("GHS", "GHS"),
                            ("GIP", "GIP"),
                            ("GTQ", "GTQ"),
                            ("GBP", "GBP"),
                            ("GNF", "GNF"),
                            ("GYD", "GYD"),
                            ("HTG", "HTG"),
                            ("HNL", "HNL"),
                            ("HKD", "HKD"),
                            ("HUF", "HUF"),
                            ("ISK", "ISK"),
                            ("IDR", "IDR"),
                            ("XDR", "XDR"),
                            ("IRR", "IRR"),
                            ("IQD", "IQD"),
                            ("ILS", "ILS"),
                            ("JMD", "JMD"),
                            ("JPY", "JPY"),
                            ("JOD", "JOD"),
                            ("KZT", "KZT"),
                            ("KES", "KES"),
                            ("KPW", "KPW"),
                            ("KRW", "KRW"),
                            ("KWD", "KWD"),
                            ("KGS", "KGS"),
                            ("LAK", "LAK"),
                            ("LBP", "LBP"),
                            ("LSL", "LSL"),
                            ("ZAR", "ZAR"),
                            ("LRD", "LRD"),
                            ("LYD", "LYD"),
                            ("CHF", "CHF"),
                            ("MOP", "MOP"),
                            ("MKD", "MKD"),
                            ("MGA", "MGA"),
                            ("MWK", "MWK"),
                            ("MYR", "MYR"),
                            ("MVR", "MVR"),
                            ("MRU", "MRU"),
                            ("MUR", "MUR"),
                            ("XUA", "XUA"),
                            ("MXN", "MXN"),
                            ("MXV", "MXV"),
                            ("MDL", "MDL"),
                            ("MNT", "MNT"),
                            ("MAD", "MAD"),
                            ("MZN", "MZN"),
                            ("MMK", "MMK"),
                            ("NAD", "NAD"),
                            ("NPR", "NPR"),
                            ("NIO", "NIO"),
                            ("NGN", "NGN"),
                            ("OMR", "OMR"),
                            ("PKR", "PKR"),
                            ("PAB", "PAB"),
                            ("PGK", "PGK"),
                            ("PYG", "PYG"),
                            ("PEN", "PEN"),
                            ("PHP", "PHP"),
                            ("PLN", "PLN"),
                            ("QAR", "QAR"),
                            ("RON", "RON"),
                            ("RUB", "RUB"),
                            ("RWF", "RWF"),
                            ("SHP", "SHP"),
                            ("WST", "WST"),
                            ("STN", "STN"),
                            ("SAR", "SAR"),
                            ("RSD", "RSD"),
                            ("SCR", "SCR"),
                            ("SLL", "SLL"),
                            ("SLE", "SLE"),
                            ("SGD", "SGD"),
                            ("XSU", "XSU"),
                            ("SBD", "SBD"),
                            ("SOS", "SOS"),
                            ("SSP", "SSP"),
                            ("LKR", "LKR"),
                            ("SDG", "SDG"),
                            ("SRD", "SRD"),
                            ("SEK", "SEK"),
                            ("CHE", "CHE"),
                            ("CHW", "CHW"),
                            ("SYP", "SYP"),
                            ("TWD", "TWD"),
                            ("TJS", "TJS"),
                            ("TZS", "TZS"),
                            ("THB", "THB"),
                            ("TOP", "TOP"),
                            ("TTD", "TTD"),
                            ("TND", "TND"),
                            ("TRY", "TRY"),
                            ("TMT", "TMT"),
                            ("UGX", "UGX"),
                            ("UAH", "UAH"),
                            ("AED", "AED"),
                            ("USN", "USN"),
                            ("UYU", "UYU"),
                            ("UYI", "UYI"),
                            ("UYW", "UYW"),
                            ("UZS", "UZS"),
                            ("VUV", "VUV"),
                            ("VES", "VES"),
                            ("VED", "VED"),
                            ("VND", "VND"),
                            ("YER", "YER"),
                            ("ZMW", "ZMW"),
                            ("ZWL", "ZWL"),
                            ("XBA", "XBA"),
                            ("XBB", "XBB"),
                            ("XBC", "XBC"),
                            ("XBD", "XBD"),
                            ("XTS", "XTS"),
                            ("XXX", "XXX"),
                            ("XAU", "XAU"),
                            ("XPD", "XPD"),
                            ("XPT", "XPT"),
                            ("XAG", "XAG"),
                        ],
                        max_length=5,
                    ),
                ),
                ("card_id", models.IntegerField(null=True)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("WITHDRAWAL", "Withdrawal"),
                            ("PAYMENT", "Payment"),
                            ("INTERNAL_TRANSFER", "Internal Transfer"),
                            ("COMISSION", "Comission"),
                            ("PAYMENT_FOR_BANK_SERVICES", "Payment For Bank Services"),
                        ],
                        default="PAYMENT",
                        max_length=30,
                    ),
                ),
                ("comment", models.TextField()),
                ("created_at", models.DateField(auto_now_add=True)),
                (
                    "account_from",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="transactions_from",
                        to="accounts.accounts",
                    ),
                ),
                (
                    "account_to",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="transactions_to",
                        to="accounts.accounts",
                    ),
                ),
            ],
        ),
        migrations.AddConstraint(
            model_name="accounts",
            constraint=models.CheckConstraint(
                check=models.Q(
                    (
                        "currency__in",
                        [
                            "AFN",
                            "EUR",
                            "ALL",
                            "DZD",
                            "USD",
                            "AOA",
                            "XCD",
                            "ARS",
                            "AMD",
                            "AWG",
                            "AUD",
                            "AZN",
                            "BSD",
                            "BHD",
                            "BDT",
                            "BBD",
                            "BYN",
                            "BZD",
                            "XOF",
                            "BMD",
                            "INR",
                            "BTN",
                            "BOB",
                            "BOV",
                            "BAM",
                            "BWP",
                            "NOK",
                            "BRL",
                            "BND",
                            "BGN",
                            "BIF",
                            "CVE",
                            "KHR",
                            "XAF",
                            "CAD",
                            "KYD",
                            "CLP",
                            "CLF",
                            "CNY",
                            "COP",
                            "COU",
                            "KMF",
                            "CDF",
                            "NZD",
                            "CRC",
                            "HRK",
                            "CUP",
                            "CUC",
                            "ANG",
                            "CZK",
                            "DKK",
                            "DJF",
                            "DOP",
                            "EGP",
                            "SVC",
                            "ERN",
                            "SZL",
                            "ETB",
                            "FKP",
                            "FJD",
                            "XPF",
                            "GMD",
                            "GEL",
                            "GHS",
                            "GIP",
                            "GTQ",
                            "GBP",
                            "GNF",
                            "GYD",
                            "HTG",
                            "HNL",
                            "HKD",
                            "HUF",
                            "ISK",
                            "IDR",
                            "XDR",
                            "IRR",
                            "IQD",
                            "ILS",
                            "JMD",
                            "JPY",
                            "JOD",
                            "KZT",
                            "KES",
                            "KPW",
                            "KRW",
                            "KWD",
                            "KGS",
                            "LAK",
                            "LBP",
                            "LSL",
                            "ZAR",
                            "LRD",
                            "LYD",
                            "CHF",
                            "MOP",
                            "MKD",
                            "MGA",
                            "MWK",
                            "MYR",
                            "MVR",
                            "MRU",
                            "MUR",
                            "XUA",
                            "MXN",
                            "MXV",
                            "MDL",
                            "MNT",
                            "MAD",
                            "MZN",
                            "MMK",
                            "NAD",
                            "NPR",
                            "NIO",
                            "NGN",
                            "OMR",
                            "PKR",
                            "PAB",
                            "PGK",
                            "PYG",
                            "PEN",
                            "PHP",
                            "PLN",
                            "QAR",
                            "RON",
                            "RUB",
                            "RWF",
                            "SHP",
                            "WST",
                            "STN",
                            "SAR",
                            "RSD",
                            "SCR",
                            "SLL",
                            "SLE",
                            "SGD",
                            "XSU",
                            "SBD",
                            "SOS",
                            "SSP",
                            "LKR",
                            "SDG",
                            "SRD",
                            "SEK",
                            "CHE",
                            "CHW",
                            "SYP",
                            "TWD",
                            "TJS",
                            "TZS",
                            "THB",
                            "TOP",
                            "TTD",
                            "TND",
                            "TRY",
                            "TMT",
                            "UGX",
                            "UAH",
                            "AED",
                            "USN",
                            "UYU",
                            "UYI",
                            "UYW",
                            "UZS",
                            "VUV",
                            "VES",
                            "VED",
                            "VND",
                            "YER",
                            "ZMW",
                            "ZWL",
                            "XBA",
                            "XBB",
                            "XBC",
                            "XBD",
                            "XTS",
                            "XXX",
                            "XAU",
                            "XPD",
                            "XPT",
                            "XAG",
                        ],
                    )
                ),
                name="valid_currency_fccounts",
            ),
        ),
        migrations.AddConstraint(
            model_name="transaction",
            constraint=models.CheckConstraint(
                check=models.Q(
                    (
                        "currency__in",
                        [
                            "AFN",
                            "EUR",
                            "ALL",
                            "DZD",
                            "USD",
                            "AOA",
                            "XCD",
                            "ARS",
                            "AMD",
                            "AWG",
                            "AUD",
                            "AZN",
                            "BSD",
                            "BHD",
                            "BDT",
                            "BBD",
                            "BYN",
                            "BZD",
                            "XOF",
                            "BMD",
                            "INR",
                            "BTN",
                            "BOB",
                            "BOV",
                            "BAM",
                            "BWP",
                            "NOK",
                            "BRL",
                            "BND",
                            "BGN",
                            "BIF",
                            "CVE",
                            "KHR",
                            "XAF",
                            "CAD",
                            "KYD",
                            "CLP",
                            "CLF",
                            "CNY",
                            "COP",
                            "COU",
                            "KMF",
                            "CDF",
                            "NZD",
                            "CRC",
                            "HRK",
                            "CUP",
                            "CUC",
                            "ANG",
                            "CZK",
                            "DKK",
                            "DJF",
                            "DOP",
                            "EGP",
                            "SVC",
                            "ERN",
                            "SZL",
                            "ETB",
                            "FKP",
                            "FJD",
                            "XPF",
                            "GMD",
                            "GEL",
                            "GHS",
                            "GIP",
                            "GTQ",
                            "GBP",
                            "GNF",
                            "GYD",
                            "HTG",
                            "HNL",
                            "HKD",
                            "HUF",
                            "ISK",
                            "IDR",
                            "XDR",
                            "IRR",
                            "IQD",
                            "ILS",
                            "JMD",
                            "JPY",
                            "JOD",
                            "KZT",
                            "KES",
                            "KPW",
                            "KRW",
                            "KWD",
                            "KGS",
                            "LAK",
                            "LBP",
                            "LSL",
                            "ZAR",
                            "LRD",
                            "LYD",
                            "CHF",
                            "MOP",
                            "MKD",
                            "MGA",
                            "MWK",
                            "MYR",
                            "MVR",
                            "MRU",
                            "MUR",
                            "XUA",
                            "MXN",
                            "MXV",
                            "MDL",
                            "MNT",
                            "MAD",
                            "MZN",
                            "MMK",
                            "NAD",
                            "NPR",
                            "NIO",
                            "NGN",
                            "OMR",
                            "PKR",
                            "PAB",
                            "PGK",
                            "PYG",
                            "PEN",
                            "PHP",
                            "PLN",
                            "QAR",
                            "RON",
                            "RUB",
                            "RWF",
                            "SHP",
                            "WST",
                            "STN",
                            "SAR",
                            "RSD",
                            "SCR",
                            "SLL",
                            "SLE",
                            "SGD",
                            "XSU",
                            "SBD",
                            "SOS",
                            "SSP",
                            "LKR",
                            "SDG",
                            "SRD",
                            "SEK",
                            "CHE",
                            "CHW",
                            "SYP",
                            "TWD",
                            "TJS",
                            "TZS",
                            "THB",
                            "TOP",
                            "TTD",
                            "TND",
                            "TRY",
                            "TMT",
                            "UGX",
                            "UAH",
                            "AED",
                            "USN",
                            "UYU",
                            "UYI",
                            "UYW",
                            "UZS",
                            "VUV",
                            "VES",
                            "VED",
                            "VND",
                            "YER",
                            "ZMW",
                            "ZWL",
                            "XBA",
                            "XBB",
                            "XBC",
                            "XBD",
                            "XTS",
                            "XXX",
                            "XAU",
                            "XPD",
                            "XPT",
                            "XAG",
                        ],
                    )
                ),
                name="valid_currency_transaction",
            ),
        ),
    ]
