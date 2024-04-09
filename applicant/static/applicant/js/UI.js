$("#id_rus_mark, #id_bel_mark, #id_math_mark").on("change", function () {
    let rus_mark = 0;
    let bel_mark = 0;
    let math_mark = 0;
    if ($("#id_rus_mark").val()) {
        rus_mark = parseInt($("#id_rus_mark").val())
    }
    if ($("#id_bel_mark").val()) {
        bel_mark = parseInt($("#id_bel_mark").val())
    }
    if ($("#id_math_mark").val()) {
        math_mark = parseInt($("#id_math_mark").val())
    }

    let sum = rus_mark + bel_mark + math_mark;
    $("#id_sum_mark").val(sum);
});

