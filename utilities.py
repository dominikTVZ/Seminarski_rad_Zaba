


def unos_iznosa(poruka):
    while True:
        try:
            broj = float(input(poruka))
            if broj < 0:
                raise Exception('Morate upisati realni broj!')

        except ValueError:
            print('Unesli ste znak a ne realni broj.')
        except Exception as e:
            print(e)
        else:
            return broj

