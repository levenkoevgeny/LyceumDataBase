let language_for_dictation_elem = $("#id_language_for_dictation")
let rus_mark_elem = $("#id_rus_mark")
let bel_mark_elem = $("#id_bel_mark")
let math_mark_elem = $("#id_math_mark")
let average_mark_elem = $("#id_average_mark")
let average_mark_year_elem = $("#id_average_mark_year")
let sum_mark_elem = $("#id_sum_mark")
let fit_elem = $("#id_fit")
let diagnosis_elem = $("#id_fit_diagnosis")

function init_update_form() {
    on_class_he_goes_to_change();
    on_language_for_dictation_change();
    on_fit_change();
}

function on_fit_change() {
    let fit_elem_id = fit_elem.val();
    diagnosis_elem.prop("disabled", true).prop("required", false);
    if (parseInt(fit_elem_id) === 1) {
        diagnosis_elem.prop("disabled", true).prop("required", false).val('');
    }
    if (parseInt(fit_elem_id) === 2) {
        diagnosis_elem.prop("disabled", false).prop("required", true);
    }
}

function on_mark_change() {
    let rus_mark = 0;
    let bel_mark = 0;
    let math_mark = 0;
    if (rus_mark_elem.val()) {
        rus_mark = parseInt($("#id_rus_mark").val())
    }
    if (bel_mark_elem.val()) {
        bel_mark = parseInt($("#id_bel_mark").val())
    }
    if (math_mark_elem.val()) {
        math_mark = parseInt($("#id_math_mark").val())
    }

    let sum = rus_mark + bel_mark + math_mark;
    $("#id_sum_mark").val(sum);
}


rus_mark_elem.on("change", function () {
    on_mark_change();
});

bel_mark_elem.on("change", function () {
    on_mark_change();
});

math_mark_elem.on("change", function () {
    on_mark_change();
});

fit_elem.on("change", function () {
    on_fit_change();
});

function on_class_he_goes_to_change() {
    let arr1 = ['7 класс', '8 класс', '9 класс']
    let arr2 = ['10 класс']

    let select_text = $("#id_class_he_goes_to option:selected").text();

    average_mark_elem.prop("disabled", true).prop("required", false);
    average_mark_year_elem.prop("disabled", true).prop("required", false);

    if (arr1.includes(select_text)) {
        average_mark_elem.prop("disabled", true).prop("required", false).val('');
        average_mark_year_elem.prop("disabled", false).prop("required", true);
        $("#div_there_is_certificate_of_education").css("display", "none");
        $("#div_there_is_mark_sheet").css("display", "block");
    }

    if (arr2.includes(select_text)) {
        average_mark_elem.prop("disabled", false).prop("required", true);
        average_mark_year_elem.prop("disabled", true).prop("required", false).val('');
        $("#div_there_is_certificate_of_education").css("display", "block");
        $("#div_there_is_mark_sheet").css("display", "none");
    }
}


function on_language_for_dictation_change() {
    let id_language_for_dictation = language_for_dictation_elem.val();
    rus_mark_elem.prop("disabled", true);
    bel_mark_elem.prop("disabled", true);
    sum_mark_elem.prop("disabled", true);

    if (parseInt(id_language_for_dictation) === 1) {
        rus_mark_elem.prop("disabled", false);
        bel_mark_elem.prop("disabled", true).val('');
        sum_mark_elem.prop("disabled", false);
    }

    if (parseInt(id_language_for_dictation) === 2) {
        rus_mark_elem.prop("disabled", true).val('');
        bel_mark_elem.prop("disabled", false);
        sum_mark_elem.prop("disabled", false);
    }
}


$("#id_class_he_goes_to").on("change", function () {
    average_mark_elem.val('');
    average_mark_year_elem.val('');
    on_class_he_goes_to_change();
});

language_for_dictation_elem.on("change", function () {
    rus_mark_elem.val('');
    bel_mark_elem.val('');
    on_language_for_dictation_change()
});
