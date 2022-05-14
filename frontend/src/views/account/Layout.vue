<template>
  <div class="user-form">
    <div class="container">
      <div class="row">
        <div class="col-lg-12">
          <div class="user-form__content mx-auto">
            <router-view />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style lang="scss">
.user-form {
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;

  &__content {
    background: white;
    width: 550px;
    max-width: 100%;
    border-radius: 10px;
    padding-bottom: 20px;
    padding-top: 20px;
    padding-left: 10%;
    padding-right: 10%;
  }
}
</style>
