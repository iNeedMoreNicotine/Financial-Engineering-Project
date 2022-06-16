#include "mainForm.h"

//
// Created by 陳柏言 (Alex Chen)
//


using namespace System;
using namespace System::Windows::Forms;
[STAThread]

void main(array<String^>^ args)
{
	Application::EnableVisualStyles();
	Application::SetCompatibleTextRenderingDefault(false);
	FinAlgoProject::mainForm form;
	Application::Run(%form);

}