@extends('layouts.public')
@section('title')
    Register
@endsection

@section('page-content')

    <div class='container '>
        <div class="row">
            <form class="col s12 m9 l10" action="" method="post">
                <h2 class='header'> Register </h2>
                <p> Hanya <strong>2 menit</strong> menuju pesanan desain anda </p>
                <div class="row">
                    {{ csrf_field() }}

                    <div class="input-field col s6">
                        <i class='material-icons prefix'>account_circle</i>
                        <input placeholder="Nama anda.. " name="firstname" type="text" class="validate">
                        <label for="first_name">Nama Awal</label>
                    </div>
                    <div class="input-field col s6">
                        <input id="last_name" type="text" class="validate" name='lastname'>
                        <label for="last_name">Nama Akhir</label>
                    </div>
                </div>
                <div class="row">
                    <div class="input-field col s12">
                        <i class='material-icons prefix'>email</i>
                        <input name="email" type="email" class="validate">
                        <label>Email</label>
                    </div>
                </div>
                <div class="row">
                    <div class="input-field col s12">
                        <i class='material-icons prefix'>contact_phone</i>
                        <input id="email" type="number" name='contact' class="validate">
                        <label>No. HP / Yang bisa dihubungi</label>
                    </div>
                </div>
                <div class="row">
                    <div class="input-field col s12">
                        <i class='material-icons prefix'>vpn_key</i>
                        <input type="password" name='password'>
                        <label>Password</label>
                    </div>
                </div>
                <div class="row">
                    <div class="input-field col s12">
                        <i class='material-icons prefix'></i>
                        <input name='repassword' type='password'>
                        <label>Re-type password</label>
                    </div>
                </div>
                <button class="btn btn-large waves-light red darken-1" type="submit" name="action">Daftar Sekarang!
                    <i class="material-icons right">send</i>
                </button>

            </form>

            @include('includes.ad-sidebar')

        </div>

    </div>

@stop

@section('custom-scripts')

    <script department='text/javascript'>
        $(document).ready(function(){
            $('.modal-trigger').leanModal();
        });
    </script>
@stop
