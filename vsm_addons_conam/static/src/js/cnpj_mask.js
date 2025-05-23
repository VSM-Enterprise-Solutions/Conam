odoo.define('vsm_addons_conam.cnpj_mask', function (require) {
    "use strict";
    var fieldRegistry = require('web.field_registry');
    var basicFields = require('web.basic_fields');

    var CnpjMaskField = basicFields.FieldChar.extend({
        events: _.extend({}, basicFields.FieldChar.prototype.events, {
            'input': '_onInput',
            'keyup': '_onInput',
            'change': '_onInput',
            'blur': '_onInput',
        }),

        _onInput: function (event) {
            var value = event.target.value.replace(/\D/g, '');
            if (value.length > 14) value = value.slice(0, 14);
            if (value.length > 12)
                value = value.replace(/^(\d{2})(\d{3})(\d{3})(\d{4})(\d{2}).*/, "$1.$2.$3/$4-$5");
            else if (value.length > 8)
                value = value.replace(/^(\d{2})(\d{3})(\d{3})(\d{0,4})/, "$1.$2.$3/$4");
            else if (value.length > 5)
                value = value.replace(/^(\d{2})(\d{3})(\d{0,3})/, "$1.$2.$3");
            else if (value.length > 2)
                value = value.replace(/^(\d{2})(\d{0,3})/, "$1.$2");
            event.target.value = value;
            this._setValue(value);
        },
    });

    fieldRegistry.add('cnpj_mask', CnpjMaskField);
}); 