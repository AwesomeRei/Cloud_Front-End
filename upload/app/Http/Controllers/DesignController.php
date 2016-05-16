<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use App\User;
use App\Design;
use App\Type;
class DesignController extends Controller
{
//            1->poster, 2->video, 3-> 3d, 4 -> website
    public function index()
    {
        $data['items'] = Design::get();
        return view('design.index', $data);
    }

    public function create(Request $request)
    {
        if($request->isMethod('get')){
            $data['types'] = Type::get();
            return view('design.create', $data);
        }
        elseif($request->isMethod('post')){

            dd($request->all);
            $get = $request->all();

        }

    }

    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        //
    }
}
