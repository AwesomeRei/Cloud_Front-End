<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Http\Requests;
use App\Http\Controllers\Controller;
use App\User;

class DesignerController extends Controller
{

    public function index()
    {
        $this->data['items'] =User::where('role',2)->get();

        return view('designer.index', $this->data);
    }


    public function create(Request $request)
    {
        if($request->isMethod('get')){
            return view('designer.create');
        }
        else if($request->isMethod('post')){

            User::create($request->all());
            return redirect('designer');
        }
    }

    public function detail($id)
    {
        $data['user'] = User::find($id);
        return view('designer.detail', $data);
    }

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
        if($request->isMethod('get')){
            $data['user'] = User::find($id);
//            dd($data);
            return view('designer.update', $data);
        }
        else if($request->isMethod('post')){
            $updatedUser = User::find($id);
            if($updatedUser->update($request-all)){
                return redirect('designer/detail'.$id);
            }
        }
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
