# Ваш токен доступа ВК
TOKEN = 'N3AKHv9_KrIn5zfLVHZVvOiL1tveu7tmYS1qneev_R0G7HkXM46dxRSA1Vcrx1GNM30Cg9ueU7l50G2JywV-psb1wlW2vWXU9HON-qrtgbAB8sPhzPP9V3fquHE-b97AvCd-iQCm0-EoqMDY167voMc-BM2t0bq0L4my_QpVs5n3VXI5bLvP_SHBCcf3ZYKzrlsXolvod_pC-2zoc6T3uQ'

# Версия ВК API
VERSION = 5.199

# Директория, где будут храниться номера телефонов
DUMP_DIRECTORY = 'dumps'

FILTERS = {
    # Минимальное количество цифр в номере телефона
    'min_digits_count': 10,

    # Номера телефонов которые будут игнорироваться
    'ignored_phones': (
        '88005553535', '8-800-555-35-35'
    )
}
