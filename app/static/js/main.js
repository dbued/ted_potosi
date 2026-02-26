$(function () {
  // Cerrar sidebar automáticamente en móviles al hacer clic en un enlace
  if ($(window).width() < 768) {
    $('#sidebarMenu .nav-link').on('click', function() {
      $('#sidebarMenu').collapse('hide');
    });
  }

  // Inicializar tooltips si se usan
  $('[data-toggle="tooltip"]').tooltip();
});