class DatabaseRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'ctt_api':
            if model._meta.db_table == 'case_tt':
                return 'ctt'
            if model._meta.db_table == 'msisdn_imsi':
                return 'datacollector'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'ctt_api':
            if model._meta.db_table == 'msisdn_imsi':
                return 'datacollector'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return True

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        return None
